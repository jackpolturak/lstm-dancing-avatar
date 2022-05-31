import numpy as np 
import tensorflow  as tf
from preprocess import Preprocessor
import pandas as pd

from keras.losses import mean_absolute_error as mse
preprocess = Preprocessor()
train_X, train_Y, test_X, test_Y = preprocess.import_normalize()



import matplotlib.pyplot as plt


def sanity_sequence_check(test_X, test_Y, model):

	print('Input', test_X[0])
	print('Correct', test_Y[0])
	print('Prediction', model(test_X[0][None,...]))

	print('Input', test_X[3])
	print('Correct', test_Y[3])
	print('Prediction', model(test_X[3][None,...]))



def plot_prediction(train_Y):

	print("Loading Model...")
	new_model = tf.keras.models.load_model('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/Kab')
	print("Model loaded! :)")

	print("Predicting...")
	ypred = new_model.predict(train_X)
	ypred = np.squeeze(ypred)
	train_Y = np.squeeze(train_Y)

	plt.title("Model prediction on validation data")
	x_ax = range(len(train_Y))

	print("Plotting...")
	plt.scatter(x_ax, train_Y[:,10],  s=6, label="THUMB_X validation")
	plt.plot(x_ax, ypred[:, 10], label="THUMB_X model prediction")
	plt.legend()

	print("Showing plot...")
	plt.show()



#model, trainx, trainy
def plot_generated_vs_tain(trainy):

    print("Calling plot_generated_vs_tain...")

    generated_dataset = "/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/Generated CSVs/MRCT(start=).csv"
    data = pd.read_csv(generated_dataset)   

    generated_dataset = data.to_numpy()
    print("-")
    print(len(generated_dataset))
    

    trainy = np.squeeze(trainy)

    #slice trainy
    trainy = trainy[0:len(generated_dataset)]
    x_ax = range(len(trainy))


    print("trainY shape")
    print(trainy.shape)
    

    plt.scatter(x_ax, trainy [:,1],  s=6, label="training data")
    plt.plot(x_ax, generated_dataset[:, 1], label="generated predictions")
    plt.show()


    return 




plot_prediction(train_Y)

# new_model = tf.keras.models.load_model('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/Techno: 3')