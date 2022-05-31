# importing pandas
import pandas as pd  
import os

dirname = os.path.dirname(__file__)


#DANCE
dance_df = pd.read_csv(f"{dirname}/"+"CSVs/Dance CSVs/Kab")

print("POSE DATA")
print(dance_df.head())

#SOUND
sound_df = pd.read_csv(f"{dirname}/"+"CSVs/Music CSVs/Kab.csv")
# df.reset_index(drop=True, inplace=True)
# df1.reset_index(drop=True, inplace=True)

print("SOUND DATA")
print(sound_df.head())

#MERGRED
combined_df = pd.concat([dance_df, sound_df], axis=1)
combined_df.dropna(inplace=True)
print("COMBINED DATA")
print(combined_df.head(20))

combined_df.to_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Kab.csv", index=False)


