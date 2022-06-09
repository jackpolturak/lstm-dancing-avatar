# importing pandas
import pandas as pd  
import os

dirname = os.path.dirname(__file__)


#DANCE
dance_df = pd.read_csv(f"{dirname}/"+"CSVs/Dance CSVs/Kab_untrained_higher.csv")

print("POSE DATA")
print(dance_df.head())

#SOUND
sound_df = pd.read_csv(f"{dirname}/"+"CSVs/Music CSVs/Kab_untrained_higher2.csv")
# df.reset_index(drop=True, inplace=True)
# df1.reset_index(drop=True, inplace=True)

print("SOUND DATA")
print(sound_df)

#MERGRED
combined_df = pd.concat([dance_df, sound_df], axis=1)
#combined_df.dropna(inplace=True)
print("COMBINED DATA")
print(combined_df.head(100))

combined_df = combined_df.loc[6:1000, :]

print("combined slice")
print(combined_df.head(170))

combined_df.to_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Kab_untrained_higher.csv", index=False)


