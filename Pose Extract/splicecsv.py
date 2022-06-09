# importing pandas

import pandas as pd  
import os

dirname = os.path.dirname(__file__)


#DANCE
# train_df = pd.read_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Techno: The Boys.csv")
train_df = pd.read_csv("/Users/jackpolturak/Documents/GitHub/lstm-dancing-avatar/Pose data/CSVs/Combined CSVs (Dance + Music)/Kab.csv")

#Splice the DF to the same length as generated output for comparison

# train_df = train_df[:1500, :]
train_df = train_df.loc[0:3500, :]
print(train_df)

# train_df.to_csv(f"{dirname}/"+'CSVs/Spliced CSVs/KAB_TRAIN.csv', index=False) # save the data as a csv file no index





        
import matplotlib.pyplot as plt

train_df = train_df.to_numpy()
train_df = train_df[0:800]
fig, axs = plt.subplots(2)


x_ax = range(len(train_df))
fig.suptitle("Comparing audio and pose features:")
axs[1].plot(x_ax, train_df[:,0])
axs[0].plot(x_ax, train_df[:,109])
axs[1].set(xlabel='Frame Number', ylabel='Nose Postion Y')
axs[0].set(xlabel='Frame Number', ylabel='Energy Band Low')
plt.show()