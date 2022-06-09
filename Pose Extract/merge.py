#THIS CODE COMBINES POSE DATA WITH EXTRACRED MUSIC FEATURES
# ONCE MUSIC FEATURES HAVE BEEN EXTRACTED from  /Music Extract/audio_features.py
#This code then combines all data so that is ready for machine learning preprocessing 

import pandas as pd  
import os

dirname = os.path.dirname(__file__)
#DANCE
dance_df = pd.read_csv(f"{dirname}/"+"CSVs/Dance CSVs/Kab_untrained_higher.csv")

#SOUND
sound_df = pd.read_csv(f"{dirname}/"+"CSVs/Music CSVs/Kab_untrained_higher2.csv")

#MERGRED
combined_df = pd.concat([dance_df, sound_df], axis=1)
combined_df.to_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Kab_untrained_higher.csv", index=False)


#FOR TESTING WITH UNTRAINED SONGS ONLY:

# combined_df = combined_df.loc[6:1000, :]
# combined_df.to_csv(f"{dirname}/"+"CSVs/Combined CSVs (Dance + Music)/Kab_untrained_higher.csv", index=False)

