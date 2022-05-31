# importing pandas
import pandas as pd  
import os

dirname = os.path.dirname(__file__)


#DANCE
train_df = pd.read_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Techno: The Boys.csv")

#Splice the DF to the same length as generated output for comparison

# train_df = train_df[:1500, :]
train_df = train_df.loc[6085:6085+800, :]
print(train_df)

train_df.to_csv(f"{dirname}/"+'CSVs/Spliced CSVs/Techo: The Boys.csv', index=False) # save the data as a csv file no index



        

