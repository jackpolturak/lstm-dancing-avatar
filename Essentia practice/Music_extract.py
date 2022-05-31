from audioop import rms
import essentia.standard as es
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os




#Load audio:
audio_file = '/Users/jackpolturak/Documents/GitHub/dancing-avatar/Pose data/Dance Videos/Techno-the-boys.mp3'
audio = es.MonoLoader(filename=audio_file)()




windowing = es.Windowing(type='hamming')


barkbands = es.BarkBands()
tristimulus = es.Tristimulus()
distributiion_shape = es.DistributionShape()
central_moments = es.CentralMoments()


#Spectral features 
spectrum = es.Spectrum()

centroid = es.SpectralCentroidTime()
roll_off = es.RollOff()
spectrum = es.Spectrum()
crest = es.Crest()
complexity = es.SpectralComplexity()
flux = es.Flux()

ERBband = es.ERBBands()




#Melodic Algos
pitchSAL = es.PitchSalience()
inharmonicity = es.Inharmonicity()
dissonance = es.Dissonance()


#TRIMBAL



sample_rate = 44100
hopsize = int(sample_rate/30.0)
print(hopsize)
frame_size = 2942

mfcc_extractor = es.MFCC(inputSize=1472)



# roll_off = []

bark_band_list = list()
roll_off_list = list()
mfcc_list = list()
crest_list = list()
pitch_SAL_list = list()
dissonance_list = list()
complexity_list = list()
distributiion_shape_list = list()
flux_list = list()


n = 0


#frame size of 66.7ms:  (44,100/1000)*66.7 ---- make sure it's even 
frame_size = 2942
for frame in es.FrameGenerator(audio, frameSize=frame_size, hopSize=hopsize, startFromZero=False):
    frame_spectrum = spectrum(windowing(frame))

    # print(frame_spectrum.shape)

    frame_roll_off = roll_off(frame_spectrum)
    frame_flux = flux(frame_spectrum)
    frame_barkbands = barkbands(frame_spectrum)
    bands_mfcc,frame_mfcc = mfcc_extractor(frame_spectrum)
    frame_crest = crest(frame_spectrum)
    frame_pitch_SAL = pitchSAL(frame_spectrum)
    frame_complexity = complexity(frame_spectrum)


    mfcc_list.append(frame_mfcc)
    roll_off_list.append(frame_roll_off)
    bark_band_list.append(frame_barkbands)
    #mfcc_list.append(frame_mfcc)
    crest_list.append(frame_crest)
    pitch_SAL_list.append(frame_pitch_SAL)
    complexity_list.append(frame_complexity)
    flux_list.append(frame_flux)
    
#PITCH
pitch_extractor = es.PredominantPitchMelodia(frameSize=frame_size, hopSize=hopsize)
pitch_values, pitch_confidence = pitch_extractor(audio)
pitch_list = np.linspace(0.0,len(audio)/44100.0,len(pitch_values))

# print(pitch_values)

# #MFCC
# mfcc_extractor = es.MFCC(frameSize=frame_size, hopSize=hopsize)
# one, two = mfcc_extractor(audio)
# mfcc_list = np.linspace(0.0,len(audio)/44100.0,len(one))
# print("MFCC list shape ")
# print(mfcc_list.shape)


crest_list= np.array(crest_list)
pitch_SAL_list= np.array(pitch_SAL_list)
complexity_list = np.array(complexity_list)
roll_off_list = np.array(roll_off_list)
bark_band_list = np.array(bark_band_list)
flux_list = np.array(flux_list)
mfcc_list = np.array(mfcc_list)

print("SHAPEEE")
print(bark_band_list.shape)
# print(flux_list.shape)



df_bark = pd.DataFrame(bark_band_list)
df_roll = pd.DataFrame(roll_off_list)
df_mfcc = pd.DataFrame(mfcc_list)
df_crest = pd.DataFrame(crest_list)
df_pitch_SAL = pd.DataFrame(pitch_SAL_list)
df_complexity = pd.DataFrame(complexity_list)
df_flux = pd.DataFrame(flux_list)
df_pitch = pd.DataFrame(pitch_list)


# plt.plot(df_mfcc)
# plt.show()




combined_df = pd.concat([df_bark, df_roll, df_crest, df_pitch_SAL, df_complexity, df_flux, df_pitch, df_mfcc], axis=1)


# print(combined_df.tail())
combined_df.to_csv('/Users/jackpolturak/Documents/GitHub/dancing-avatar/Pose data/CSVs/Music CSVs/Techno:The Boys.csv', index=False)




low_level_specrtrum = es.LowLevelSpectralExtractor(frameSize=frame_size, hopSize=hopsize, sampleRate=sample_rate)
low_level_specrtrum_extract = low_level_specrtrum(audio)

barkbands = low_level_specrtrum_extract[0]
barkbands_kurtosis = low_level_specrtrum_extract[1]
barkbands_skewness = low_level_specrtrum_extract[2]
barkbands_spread = low_level_specrtrum_extract[3]
hfc = low_level_specrtrum_extract[4]
mfcc = low_level_specrtrum_extract[5]
pitch = low_level_specrtrum_extract[6]
pitch_salience = low_level_specrtrum_extract[7]

pitch_sal = low_level_specrtrum_extract[8]

