#Various plotting functions for sanity checks

from turtle import color
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
    new_model = tf.keras.models.load_model('model simple-lstm/Kab')
    print("Model loaded! :)")

    print("Predicting...")
    ypred = new_model.predict(train_X)
    ypred = np.squeeze(ypred)
    train_Y = np.squeeze(train_Y)

    plt.title("Model 2 Prediction on Training Data")
    x_ax = range(len(train_Y))

    print("Plotting...")
    plt.scatter(x_ax, train_Y[:,10],  s=6, label="THUMB_X Training")
    plt.plot(x_ax, ypred[:, 10], label="THUMB_X model prediction")
    plt.xlabel("Frame (int)")
    plt.ylabel('Normalized features value')
    plt.legend()

    print("Showing plot...")
    plt.show()



#model, trainx, trainy
def plot_generated_vs_tain(trainy):

    print("Calling plot_generated_vs_tain...")

    generated_dataset = "multi-cnn lstm.csv"
    train_data = 'Kab.csv'
    train_data = pd.read_csv(train_data)
    data = pd.read_csv(generated_dataset)   

    generated_dataset = data.to_numpy()
    train_data = train_data.to_numpy()
    print("-")


    
    print(len(generated_dataset))
    

    trainy = np.squeeze(trainy)

    #slice trainy
    train_data = train_data[0:len(generated_dataset)]
    x_ax = range(len(generated_dataset))


    print("trainY shape")
    print(trainy.shape)
    
    plt.title("Model 3 Generated Dance vs Training Data:")
    plt.plot(x_ax, train_data [:,47],  label="training data: LEFT_WRIST_X", color='blue')
    plt.plot(x_ax, generated_dataset[:, 47], label="generated predictions: LEFT_WRIST_X", color='red')
    plt.xlabel("Frame (int)")
    plt.ylabel('Normalized features value')
    plt.legend()
    plt.show()


    return 




# plot_prediction(train_Y)

plot_generated_vs_tain(train_Y)
