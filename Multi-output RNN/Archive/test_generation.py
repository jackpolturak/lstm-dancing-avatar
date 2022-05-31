
# from msilib import sequence
from pyparsing import original_text_for
import tensorflow  as tf
from preprocess import Preprocessor, SCALER
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



new_model = tf.keras.models.load_model('/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Multi-output RNN/saved_model/my_model')

new_model.summary()

preprocess = Preprocessor()

# train_X, train_Y, test_X, test_Y  = preprocess.import_normalize()
train_X, train_Y = preprocess.import_normalize()




print("first seqeunce to be passed in:")
first_sequence = train_X[0]
print(first_sequence)
generated_sequence_list = []

sequence_length = 10


generation_number = 0

ypred = new_model.predict(first_sequence[None,...])

print("Model output: ")

ypred = np.squeeze(ypred)

print(ypred)

print("second sequence to be passed:")
print(train_X[1])

print("second sequence to be passed in LASTEST VAL:")


next_music = train_X[1][-1]
print(next_music)


count = 0
for i in range(len(ypred)):
    next_music[count] = ypred[count]
   
    count +=1

print("new input row :")
print(next_music)



# print("firat seqeunce np rolles")
# first_sequence = np.roll(first_sequence, -1, axis=0)
# print(first_sequence)