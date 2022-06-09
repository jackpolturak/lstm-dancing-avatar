
from locale import normalize
import re
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# import plotly.graph_objects as go
import matplotlib.pyplot as plt




NUMBER_FEATURES = 168
NUMBER_LABELS = 99
FORECAST_HORIZON= 1
LOOK_BACK = 30
SCALER = MinMaxScaler()


LABEL_SCALER = MinMaxScaler()

class Preprocessor:

    def __init__(self):
        self.look_back = LOOK_BACK
        self.forecast_horizon = FORECAST_HORIZON
        self.number_features = NUMBER_FEATURES
        
    
    
    def import_normalize(self):
        main_df = pd.DataFrame()
        dataset = "Kab.csv"

        df = pd.read_csv(dataset)

        if len(main_df) == 0:
         main_df = df
        else:
            main_df = main_df.join(df)

    

        #Split test and train
        times = sorted(df.index.values)
        last_90pct = times[-int(0.095*len(times))]

        print("Last 90")
        print(last_90pct)

        validation_main_df = main_df[(main_df.index >= last_90pct)]  # make the validation data where the index is in the last 5%
        # main_df = main_df[(main_df.index < last_90pct)]  # now the main_df is all the data up to the last 5% 
    

        #THIS IS ONLY TO DESCAL:ES
        # Select first N columns
        label_collums  = main_df.iloc[: , :NUMBER_LABELS]
        scaled_labels_only = LABEL_SCALER.fit_transform(label_collums)
        

        scaled_train = SCALER.fit_transform(main_df)
        scaled_validation = SCALER.transform(validation_main_df)


        # print(scaled_train[:, 99:130])
        # train_X, train_Y = self.split_sequence(scaled_train, self.look_back, self.forecast_horizon)
        # train_X, train_Y = self.split_sequence(scaled_train, self.look_back, self.forecast_horizon)
        #test_X, test_Y =  self.split_sequence(scaled_validation, self.look_back, self.forecast_horizon)
    

        train_X, train_Y = self.split_sequence(scaled_train, self.look_back, self.forecast_horizon)
        test_X, test_Y =  self.split_sequence(scaled_validation, self.look_back, self.forecast_horizon)


        return train_X, train_Y, test_X, test_Y



    #Split sequences into the appropriate format for lstm
    def split_sequence(self, sequence, look_back, forecast_horizon):
        X, y = list(), list()

        for i in range(len(sequence)):
            lag_end = i + look_back
            forecast_end = lag_end + forecast_horizon
            if forecast_end > len(sequence):
                break
            seq_x, seq_y = sequence[i:lag_end], sequence[lag_end:forecast_end]
            
            X.append(seq_x)
            y.append(seq_y)

        X = np.array(X)
        y = np.array(y)


        # DROP MUSIC DATA FROM Y LABEL!
        y_sqeeze = np.squeeze(y)
        new_y = np.delete(y_sqeeze, slice(NUMBER_LABELS, NUMBER_FEATURES), axis=1)
        y_unsquueze  = np.expand_dims(new_y, axis=1)


        return X, y_unsquueze
