
from pyparsing import original_text_for
import tensorflow  as tf
from preprocess import NUMBER_FEATURES
from preprocess import Preprocessor, SCALER, LABEL_SCALER
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




#model = tf.keras.models.load_model('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/Techno: 3')

#new_model.summary()

preprocess = Preprocessor()

# train_X, train_Y, test_X, test_Y  = preprocess.import_normalize()
train_X, train_Y, test_X, test_Y = preprocess.import_normalize()

print(test_X.shape)


#This function takes the output at T and rolls it back into the sequence at t+1
def generate_sequences(train_X, new_model, sequence_length):

    #From where do you want to start generating
    generation_number = 0
    print("FIRST SEQUENCE TO BE USED: Train_X[0]")

    first_sequence = train_X[generation_number]
    print(first_sequence)
    #extract all ypred values into a list
    generated_sequence_list = []

    
    print("Entering loop")
    for i in range(sequence_length):
        # generation_number +=1


        ypred = new_model.predict(first_sequence[None,...])
        
        generation_number +=1
        print("YPRED:")
        ypred = np.squeeze(ypred)

        print(ypred)

        
        next_music_sequence = train_X[generation_number][-1]
        print("Next ACCURATE music data ")
        print(next_music_sequence)


        count = 0 
        #for i in range(len(ypred)):
        for i in range(99):
            next_music_sequence[count] = ypred[count]
            count +=1


        print("Next msuic seqeunce only changing input vals:")
        print(next_music_sequence)

        #ADD GENERATED PREDICTION INTO THE THIS

        generated_sequence_list.append(ypred)
        #print(generated_sequence_list)

        #ROLL SEQUENCE BACK
        print("Firat seqeunce before roll ")
        print(first_sequence)
        first_sequence = np.roll(first_sequence, -1, axis=0)


        print("Firat seqeunce bafter roll ")

        print(first_sequence)



        #ADD NEW PREDICTION TO THE END OF THE SEQUENCE - SHIFT ALL BACK

        
        first_sequence[-1] = next_music_sequence
        
        print("New sequence that will  next be used in model")
        print(first_sequence)        
        # print("New seqeunce")
        # print(first_sequence)


    #Convert list into an array 
    generated_sequence_list = np.array(generated_sequence_list)

    print(generated_sequence_list)
  
    #print("Generated seqeunce list ARRAY CONVERTED")
    #print(generated_sequence_list)

    #np squeeze testY
    #test_Y = np.squeeze(train_Y)

    #plt.title("self generated thumb movement prediction, sequence length = 100")

    x_ax = range(sequence_length)
    # plt.plot(x_ax, generated_sequence_list[:, 50], label="Thumb position: recursive-model-prediction")
    # plt.plot(x_ax,  test_Y[:, 50], label="test_Y[0]")

    # plt.xlabel('Time steps')
    # plt.ylabel('Recursive prediction')
    # plt.legend()
    # plt.show()

    #INVERSE TRANFORM THE SCALED DATA
    # unscale_sequences = SCALER.inverse_transform(generate_sequences)
    # print(unscale_sequences)


    df = pd.DataFrame(generated_sequence_list)
    print("DATAFRAME OF GENERATED SEQUENCES")
    print(df)
    df_descaled = LABEL_SCALER.inverse_transform(df)
    df_descaled = pd.DataFrame(df_descaled)



    #df_descaled.to_csv("/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/Generated CSVs/MCRT3_multihead.csv", index=False)
    return generated_sequence_list



def generate_sequence_multi_head(train_X, new_model, sequence_length):

    generation_number = 0

    #SANITY CHECK:
    current = train_X[generation_number]
    
    print("input sequence shape")
    input_sequence = train_X[generation_number]
    print(input_sequence.shape)

    #Initialize sequence list - will; be the csv
    sequence_list = input_sequence
    print("rolling sequence_list shape")


    print("Entering loop")
    for i in range(sequence_length):
        generation_number +=1
        ypred = new_model.predict(input_sequence[None,...])
        ypred = np.squeeze(ypred)
        print("ypred")
        print(ypred)

        next_input_frame = train_X[generation_number][-1]
        print("next_input_frame")
        print(next_input_frame)

        count = 0 
        #for i in range(len(ypred)):

        for i in range(99):
            next_input_frame[count] = ypred[count]
            count +=1

        print("next input frame after replacing only first 99 movement data")
        print(type(next_input_frame))

        sequence_list  = np.vstack([sequence_list, next_input_frame])

        print("New sequence list shape")
        print(sequence_list.shape)

        input_sequence = np.roll(input_sequence, -1, axis=0)
        input_sequence[-1] = next_input_frame
    
    print("Final sequence liast")
    print(sequence_list.shape)

    df = pd.DataFrame(sequence_list)
    print("DATAFRAME OF GENERATED SEQUENCES")
    print(df)
    df_descaled = LABEL_SCALER.inverse_transform(df)
    df_descaled = pd.DataFrame(df_descaled)


    #Apply moving average filter to smooth visualisation
    rolling =  df_descaled.rolling(window=5)
    df_descaled= rolling.mean()
    df_descaled.dropna(inplace=True)

    df_descaled.to_csv("/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/Generated CSVs 2/Techo:The Boys.csv", index=False)

    return 


def generate_dance(train_X, sequence_length):

    #Load model 
    model = tf.keras.models.load_model('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/saved_models 2/Techno: 3')

    frame_generation_number = 6085
    input_sequence = train_X[frame_generation_number]


    #Splice just the first sequence of movement to initalize
    generated_dance_sequence = input_sequence[:, :99]

    for i in range(sequence_length):
        print(input_sequence)
        ypred = model.predict(input_sequence[None,...])
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

    df_descaled.to_csv("/Users/jackpolturak/Documents/GitHub/dancing-avatar/Multi-output RNN/Generated CSVs 2/Techo: 3.csv", index=False)

    return 




generate_dance(train_X, sequence_length=800)

