#This is where the network is trained and save 



from cgi import test
from gc import callbacks
from operator import mod
from pyexpat import model
from time import process_time_ns
from unicodedata import name
from xml.etree.ElementTree import TreeBuilder
import numpy as np 
from preprocess import Preprocessor
import tensorflow  as tf

from keras import Sequential
from keras.layers import LSTM, CuDNNLSTM,Dense, Dropout, TimeDistributed, Conv1D, MaxPooling1D, Flatten, Bidirectional, Input, Flatten, Activation, Reshape, RepeatVector, Concatenate, BatchNormalization, LayerNormalization, LeakyReLU
from keras.models import Model
from keras.losses import MeanAbsoluteError

from keras.layers import CuDNNLSTM

from keras.losses import mean_absolute_error as mse

from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

#IMPORT GLOBAL VARIABLES
from preprocess import FORECAST_HORIZON, NUMBER_FEATURES, LOOK_BACK, NUMBER_LABELS 

preprocess = Preprocessor()
#train_X, train_Y, test_X, test_Y = preprocess.import_normalize()
train_X, train_Y, test_X, test_Y = preprocess.import_normalize()

print(train_Y.shape)


def lstm(model_name,  model_number):
	model = Sequential()	
	model.add(LSTM(300, activation='relu', input_shape=(LOOK_BACK, NUMBER_FEATURES)))
	model.add(Dropout(0.2))
	model.add(RepeatVector(FORECAST_HORIZON))
	model.add(LSTM(300, activation='relu', input_shape=(LOOK_BACK, NUMBER_FEATURES)))
	model.add(Dropout(0.2))
	model.add(RepeatVector(FORECAST_HORIZON))
	model.add(LSTM(300, activation='relu', return_sequences=True))
	model.add(Dropout(0.2))
	model.add(TimeDistributed(Dense(NUMBER_LABELS, activation='sigmoid')))
	model.compile(optimizer='adam', loss='mse')
	model.save(f'{model_number}/{model_name}')
	model.summary()

	return model


def multihead_cnn_lstm(model_name, model_number):
	input_layer = Input(shape=(LOOK_BACK,  NUMBER_FEATURES)) 
	head_list = []

	for i in range(0,  NUMBER_FEATURES):
		conv_layer_head = Conv1D(filters=3, kernel_size=3, activation='relu')(input_layer)
		conv_layer_head_2 = Conv1D(filters=1, kernel_size=3, activation='relu')(conv_layer_head)
		conv_layer_flatten = Flatten()(conv_layer_head_2)
		head_list.append(conv_layer_flatten)
	
	concat_cnn = Concatenate(axis=1)(head_list)
	reshape = Reshape((head_list[0].shape[1], NUMBER_FEATURES))(concat_cnn)

	lstm = LSTM(300, activation='relu')(reshape)
	dropout = Dropout(0.2)(lstm)
	repeat = RepeatVector(FORECAST_HORIZON)(dropout)
	
	lstm_2 = LSTM(300, activation='relu', return_sequences=True)(repeat)
	dropout = Dropout(0.2)(lstm_2)

	dense = Dense(NUMBER_LABELS, activation='sigmoid')(dropout)
	multi_head_cnn_lstm_model = Model(inputs=input_layer, outputs=dense)

	multi_head_cnn_lstm_model.compile(optimizer='adam', loss='mse', metrics='accuracy')
	multi_head_cnn_lstm_model.summary()
	multi_head_cnn_lstm_model.save(f'{model_number}/{model_name}')
	return multi_head_cnn_lstm_model


def cnn_lstm(model_name, model_number):

	model_enc_dec_cnn = Sequential()
	model_enc_dec_cnn.add(Conv1D(filters=64, kernel_size=9, activation='relu', input_shape=(LOOK_BACK, NUMBER_FEATURES)))
	model_enc_dec_cnn.add(Conv1D(filters=64, kernel_size=11, activation='relu'))
	model_enc_dec_cnn.add(MaxPooling1D(pool_size=2))
	model_enc_dec_cnn.add(Flatten())
	model_enc_dec_cnn.add(RepeatVector(FORECAST_HORIZON))
	model_enc_dec_cnn.add(LSTM(300, activation='relu'))
	model_enc_dec_cnn.add(RepeatVector(FORECAST_HORIZON))
	model_enc_dec_cnn.add(LSTM(300,activation='relu', return_sequences=True))
	model_enc_dec_cnn.add(TimeDistributed(Dense(100, activation='relu')))
	model_enc_dec_cnn.add(TimeDistributed(Dense(NUMBER_LABELS, activation='sigmoid')))
	model_enc_dec_cnn.compile(loss='mse', optimizer='adam')
	model_enc_dec_cnn.summary()
	model_enc_dec_cnn.save(f'{model_number}/{model_name}')
	return model_enc_dec_cnn


def train_model(model, model_name, model_number):

	#!DEFINE MODEL NAME: IMPORTANT!
	#Call backs 
	early_stopping_callback = EarlyStopping(monitor='loss', min_delta=0.0005, patience=17, mode='min')
	checkpoint_filepath = f'{model_number}/{model_name}/checkpoint'
	checkpoint_callback = ModelCheckpoint(filepath=checkpoint_filepath, save_weights_only=True, monitor='loss', mode='min', save_best_only=True)
	rlrop_callback = ReduceLROnPlateau(monitor='loss', factor=0.2, mode='min', patience=2, min_lr=0.000000001, cooldown=3 ,verbose=1)

	#100 epochs
	epochs = 100
	batch_size = 60
	validation = 0.1
	model.fit(train_X, train_Y, epochs=epochs, batch_size=batch_size, callbacks=[rlrop_callback,checkpoint_callback,early_stopping_callback])


	print("Saving model...")
	model.save(f'{model_number}/{model_name}')

	return model




name = "Kab"
model_name = 'cnn-lstm-double-dense'


#RUN THE FOLLOWING 
model =  cnn_lstm(model_name=name,  model_number=model_name)
model = train_model(model,  model_name=name, model_number=model_name)












