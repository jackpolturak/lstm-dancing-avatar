from audioop import rms
import essentia.standard as es
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os




#Load audio:
audio_file = '/Users/jackpolturak/Documents/GitHub/dancing-avatar/Pose data/Dance Videos/Kab.mp3'
audio = es.MonoLoader(filename=audio_file)()

sample_rate = 44100
hopsize = int(sample_rate/30.0)
print(hopsize)
frame_size = 2942


low_level_specrtrum = es.LowLevelSpectralExtractor(frameSize=frame_size, hopSize=hopsize, sampleRate=sample_rate)
low_level_specrtrum_extract = low_level_specrtrum(audio)




barkbands = low_level_specrtrum_extract[0]
barkbands_kurtosis = low_level_specrtrum_extract[1]
barkbands_skewness = low_level_specrtrum_extract[2]
barkbands_spread = low_level_specrtrum_extract[3]
hfc = low_level_specrtrum_extract[4]
mfcc = low_level_specrtrum_extract[5]
pitch = low_level_specrtrum_extract[6]
f7 = low_level_specrtrum_extract[7]
pitch_sal = low_level_specrtrum_extract[8]
f9 = low_level_specrtrum_extract[9]
f10 = low_level_specrtrum_extract[10]
f11 = low_level_specrtrum_extract[11]
spectral_complexity = low_level_specrtrum_extract[12]
spectral_crest = low_level_specrtrum_extract[13]
f14 = low_level_specrtrum_extract[14]
f15 = low_level_specrtrum_extract[15]
spectral_energyband_low = low_level_specrtrum_extract[16]
spectral_energyband_middle_low = low_level_specrtrum_extract[17]
spectral_energyband_middle_high = low_level_specrtrum_extract[18]
spectral_energyband_high = low_level_specrtrum_extract[19]
f20 = low_level_specrtrum_extract[20]
spectral_flux = low_level_specrtrum_extract[21]
spectral_rms = low_level_specrtrum_extract[22]
spectral_rolloff = low_level_specrtrum_extract[23]
f24 = low_level_specrtrum_extract[24]
f25 = low_level_specrtrum_extract[25]
inharmonicity = low_level_specrtrum_extract[26]
tristimulus = low_level_specrtrum_extract[27]
f28 = low_level_specrtrum_extract[28]


barkbands = pd.DataFrame(barkbands)
barkbands_kurtosis = pd.DataFrame(barkbands_kurtosis)
barkbands_skewness = pd.DataFrame(barkbands_skewness)
barkbands_spread = pd.DataFrame(barkbands_spread)
mfcc = pd.DataFrame(mfcc)
pitch = pd.DataFrame(pitch)
pitch_sal = pd.DataFrame(pitch_sal)
spectral_complexity = pd.DataFrame(spectral_complexity)
spectral_crest = pd.DataFrame(spectral_crest)
spectral_energyband_low  = pd.DataFrame(spectral_energyband_low)
spectral_energyband_middle_low = pd.DataFrame(spectral_energyband_middle_low)
spectral_energyband_middle_high = pd.DataFrame(spectral_energyband_middle_high)
spectral_energyband_high = pd.DataFrame(spectral_energyband_high)
spectral_flux = pd.DataFrame(spectral_flux)
spectral_rms = pd.DataFrame(spectral_rms)
spectral_flux = pd.DataFrame(spectral_flux)
spectral_rolloff = pd.DataFrame(spectral_rolloff)
inharmonicity = pd.DataFrame(inharmonicity)
tristimulus = pd.DataFrame(tristimulus)
f7 = pd.DataFrame(f7)
f9 = pd.DataFrame(f9)
f10 = pd.DataFrame(f10)
f11 = pd.DataFrame(f11)
f14 = pd.DataFrame(f14)
f15 = pd.DataFrame(f15)
f20 = pd.DataFrame(f20)
f24 = pd.DataFrame(f24)
f25 = pd.DataFrame(f25)
f28 = pd.DataFrame(f28)


combined_df = pd.concat([barkbands, barkbands_kurtosis, barkbands_skewness, 
                            barkbands_spread, mfcc ,pitch ,pitch_sal, spectral_complexity, 
                            spectral_crest,spectral_energyband_low,spectral_energyband_middle_low,
                            spectral_energyband_middle_high,spectral_energyband_high,spectral_flux,
                            spectral_rms,spectral_flux,spectral_rolloff,inharmonicity,tristimulus,
                            f7,f9,f10,f11,f14,f15,f20,f24,f25,f28], axis=1)

print(combined_df)
# plt.plot(combined_df)

# plt.show()

rolling = combined_df.rolling(window=7)
main_df = rolling.mean()


# main_df.to_csv('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Pose data/CSVs/Music CSVs/Kab.csv', index=False)
