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
from keras.layers import LSTM, Dense, Dropout, TimeDistributed, Conv1D, MaxPooling1D, Flatten, Bidirectional, Input, Flatten, Activation, Reshape, RepeatVector, Concatenate, BatchNormalization, LayerNormalization, LeakyReLU
from keras.models import Model
from keras.losses import MeanAbsoluteError
from tensorflow.python.keras.optimizer_v2 import adam as adam_v2



from keras.losses import mean_absolute_error as mse

from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import matplotlib.pyplot as plt

#IMPORT GLOBAL VARIABLES
from preprocess import FORECAST_HORIZON, NUMBER_FEATURES, LOOK_BACK, NUMBER_LABELS 

preprocess = Preprocessor()
#train_X, train_Y, test_X, test_Y = preprocess.import_normalize()
train_X, train_Y, test_X, test_Y = preprocess.import_normalize()

print(train_Y.shape)


def create_model():

	model = Sequential()	
	model.add(LSTM(100, activation='relu', input_shape=(LOOK_BACK, NUMBER_FEATURES)))
	model.add(RepeatVector(FORECAST_HORIZON))
	model.add(LSTM(100, activation='relu', return_sequences=True))
	model.add(TimeDistributed(Dense(NUMBER_LABELS, activation='sigmoid')))
	model.compile(optimizer='adam', loss='mse')

	return model


def new_model():
	input_layer = Input(shape=(LOOK_BACK,  NUMBER_FEATURES)) 
	head_list = []

	for i in range(0,  NUMBER_FEATURES):
		conv_layer_head = Conv1D(filters=4, kernel_size=7, activation='relu')(input_layer)
		conv_layer_head_2 = Conv1D(filters=6, kernel_size=11, activation='relu')(conv_layer_head)
		conv_layer_flatten = Flatten()(conv_layer_head_2)
		head_list.append(conv_layer_flatten)
	
	concat_cnn = Concatenate(axis=1)(head_list)
	reshape = Reshape((head_list[0].shape[1], NUMBER_FEATURES))(concat_cnn)
	lstm = LSTM(500, activation='relu')(reshape)
	repeat = RepeatVector(FORECAST_HORIZON)(lstm)
	lstm_2 = LSTM(300, activation='relu', return_sequences=True)(repeat)
	dropout = Dropout(0.2)(lstm_2)
	dense = Dense(NUMBER_FEATURES, activation='sigmoid')(dropout)
	multi_head_cnn_lstm_model = Model(inputs=input_layer, outputs=dense)

	multi_head_cnn_lstm_model.compile(optimizer='adam', loss='mse', metrics='accuracy')

	return multi_head_cnn_lstm_model

def new_model_layer_norm():

	print("Creating Model")
	input_layer = Input(shape=(LOOK_BACK,  NUMBER_FEATURES)) 
	head_list = []

	for i in range(0,  NUMBER_FEATURES):
		conv_layer_head = Conv1D(filters=4, kernel_size=7, activation='relu')(input_layer)
		conv_layer_head_2 = Conv1D(filters=6, kernel_size=11, activation='relu')(conv_layer_head)
		leaky_00 = LeakyReLU(alpha=0.35)(conv_layer_head_2)
		conv_layer_flatten = Flatten()(leaky_00)
		head_list.append(conv_layer_flatten)

	concat_cnn = Concatenate(axis=1)(head_list)
	layer_norm_0 = LayerNormalization()(concat_cnn)
	reshape = Reshape((head_list[0].shape[1], NUMBER_FEATURES))(layer_norm_0)

	#For dataset of 7800 , 700 nodes can cause early nans - maybe try reducing this for larger datasets
	lstm = LSTM(600, activation='relu')(reshape)
	leaky = LeakyReLU(alpha=0.35)(lstm)
	layer_norm = LayerNormalization()(leaky)
	repeat = RepeatVector(FORECAST_HORIZON)(layer_norm)
	lstm_2 = LSTM(300, activation='relu', return_sequences=True)(repeat)
	leaky2 = LeakyReLU(alpha=0.35)(lstm_2)
	dropout = Dropout(0.2)(leaky2 )
	layer_norm2 = LayerNormalization()(dropout)
	dense = Dense(NUMBER_LABELS, activation='sigmoid')(layer_norm2)
	
	multi_head_cnn_lstm_model = Model(inputs=input_layer, outputs=dense)

	#Change loss functiion to MAE
	#multi_head_cnn_lstm_model.compile(optimizer=tf.keras.optimizers.Adam(clipnorm=1.0), loss='mse')

	#START FUCKING W OPTIMIZERS
	opt = tf.keras.optimizers.SGD(learning_rate=0.007, momentum=0.9)
	opt_adam = tf.keras.optimizers.Adam(learning_rate=0.0007)

	multi_head_cnn_lstm_model.compile(optimizer=opt_adam, loss="mse", metrics="mse")

	# multi_head_cnn_lstm_model.summary()
	return multi_head_cnn_lstm_model

def train_model(model):

	#!DEFINE MODEL NAME: IMPORTANT!
	model_name = "Kab"

	#Call backs 
	early_stopping_callback = EarlyStopping(monitor='loss', min_delta=0.005, patience=10, mode='min')
	checkpoint_filepath = f'/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/{model_name}'
	checkpoint_callback = ModelCheckpoint(filepath=checkpoint_filepath, save_weights_only=False, monitor='loss', mode='min', save_best_only=True)
	rlrop_callback = ReduceLROnPlateau(monitor='loss', factor=0.2, mode='min', patience=2, min_lr=0.00000000001, cooldown=3 ,verbose=1)

	#100 epochs
	epochs = 100
	batch_size = 60
	validation = 0.1
	model.fit(train_X, train_Y, epochs=epochs, batch_size=batch_size, callbacks=[checkpoint_callback,rlrop_callback])

	print("Evaluating Model")
	# train_mse = model.evaluate(train_X, train_Y, verbose=1)

	# print("Model.evaluate: ", train_mse)
	print("Saving model...")
	model.save(f'/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/{model_name}')

	return model

model =  new_model_layer_norm()
model = train_model(model)

