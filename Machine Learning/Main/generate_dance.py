#This extrracts dance data from model 
from tabnanny import verbose
from pyparsing import original_text_for
import tensorflow  as tf
from preprocess import NUMBER_FEATURES
from preprocess import Preprocessor, SCALER, LABEL_SCALER
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Import datset from Preprocessor 
preprocess = Preprocessor()
train_X, train_Y, test_X, test_Y = preprocess.import_normalize()


#Does what it says on the tin 
def generate_dance(model_number ,train_X, sequence_length):

    #Load model 
    model = tf.keras.models.load_model(f'{model_number}/Kab')
    frame_generation_number = 0
    input_sequence = train_X[frame_generation_number]

    #Splice just the first sequence of movement to initalize
    generated_dance_sequence = input_sequence[:, :99]

    for i in range(sequence_length):
        print(input_sequence)
        ypred = model.predict(input_sequence[None,...], verbose=1)
        ypred = np.squeeze(ypred)

        #Add model prediciton to the generated dance sequence 
        generated_dance_sequence  = np.vstack([generated_dance_sequence, ypred])

        #Get the next frame (T+1) of joint position and sound data
        frame_generation_number +=1
        next_input_frame = train_X[frame_generation_number][-1]

        #Replace ONLY joint position (FIRST 99) values with the model predction, keeping the actual audio features
        count = 0
        for i in range(99):
            next_input_frame[count] = ypred[count]
            count +=1
        
        #Roll back the input sequence by 1, then add our modified next input frame to the last value 
        input_sequence = np.roll(input_sequence, -1, axis=0)
        input_sequence[-1] = next_input_frame

    #Save generated dance sequence as csv for animation 
    df = pd.DataFrame(generated_dance_sequence)
    df_descaled = LABEL_SCALER.inverse_transform(df)
    df_descaled = pd.DataFrame(df_descaled)

    #Apply moving average filter to smooth visualisation (my model isnt perfect ;)
    rolling =  df_descaled.rolling(window=5)
    df_descaled= rolling.mean()
    df_descaled.dropna(inplace=True)

    df_descaled.to_csv("cnn-lstm-double-dense.csv", index=False)
    # df_descaled.to_csv(f"KamModel{model_number}_GEN_HIGHER.csv", index=False)

    return 



model_number = 'cnn-lstm-double-dense'
generate_dance(model_number, train_X, sequence_length=3000)

