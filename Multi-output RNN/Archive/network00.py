from operator import mod
from time import process_time_ns
from xml.etree.ElementTree import TreeBuilder
import numpy as np 
from preprocess import Preprocessor

from keras import Sequential
from keras.layers import LSTM, Dense, Dropout, TimeDistributed, Conv1D, MaxPooling1D, Flatten, Bidirectional, Input, Flatten, Activation, Reshape, RepeatVector, Concatenate
from keras.models import Model


from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import matplotlib.pyplot as plt



preprocess = Preprocessor()

train_X, train_Y, test_X, test_Y  = preprocess.import_normalize()


print(train_X[0])
print("-")
print(train_Y[0])




epochs = 300
batch_size = 30
validation = 0.1
FORCAST_RANGE = 1
LOOK_BACK = 50
n_features = 10



checkpoint_filepath = 'path_to_checkpoint_filepath'
checkpoint_callback = ModelCheckpoint(
	filepath=checkpoint_filepath,
	save_weights_only=False,
	monitor='val_loss',
	mode='min',
	save_best_only=True)
early_stopping_callback = EarlyStopping(
	monitor='val_loss',
	min_delta=0.005,
	patience=10,
	mode='min'
)

rlrop_callback = ReduceLROnPlateau(monitor='val_loss', factor=0.2, mode='min', patience=3, min_lr=0.001)

model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(LOOK_BACK, n_features)))
model.add(RepeatVector(FORCAST_RANGE))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(n_features)))
model.compile(optimizer='adam', loss='mse')


model.fit(train_X, train_Y, epochs=epochs, batch_size=batch_size)


#Save entire model
model.save('/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/04/saved_model/my_model')


def sanity_sequence_check(test_X, test_Y, model):


	print('Input', test_X[0])
	print('Correct', test_Y[0])
	print('Prediction', model(test_X[0][None,...]))

	print('Input', test_X[3])
	print('Correct', test_Y[3])
	print('Prediction', model(test_X[3][None,...]))




def plot_prediction(test_Y, model):

	ypred = model.predict(test_X)
	ypred = np.squeeze(ypred)
	test_Y = np.squeeze(test_Y)

	plt.title("LSTM multi-output prediction")
	x_ax = range(len(test_Y))
	plt.scatter(x_ax, test_Y [:,0],  s=6, label="y0-validation_ THUMB")
	plt.plot(x_ax, ypred[:, 0], label="y0-model-prediction_ THUMB")
	
	# plt.scatter(x_ax, test_Y [:,3],  s=6, label="y1-validation")
	# plt.plot(x_ax, ypred[:, 3], label="y1-model-prediction")

	# plt.scatter(x_ax, test_Y [:,2],  s=6, label="y2-validation")
	# plt.plot(x_ax, ypred[:, 2], label="y2-model-prediction")

	plt.legend()
	plt.show()






#CALL FUNCTIONS
plot_prediction(test_Y, model)

# sanity_sequence_check(test_X, test_Y, model)