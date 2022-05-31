from traceback import print_list
import essentia.standard as es
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


#Load audio:
audio_file = '/Users/jackpolturak/Documents/dance-vids/Dance_to_beat.mp3'
loader = es.MonoLoader(filename='/Users/jackpolturak/Documents/dance-vids/Dance_to_beat.mp3')

audio = loader()

barkbands = es.BarkBands()
tristimulus = es.Tristimulus()
distributiion_shape = es.DistributionShape()

w = es.Windowing(type='hann')
#Spectral features 
spectrum = es.Spectrum()
mfcc = es.MFCC()
centroid = es.SpectralCentroidTime()
roll_off = es.RollOff()
spectrum = es.Spectrum()
crest = es.Crest()
complexity = es.SpectralComplexity()






#Melodic Algos
pitchSAL = es.PitchSalience()
inharmonicity  =es.Inharmonicity()
dissonance = es.Dissonance()




mfccs = []
melbands = []
frameSize = 1024


sample_rate = 44100
hopSize = int(sample_rate/28)
print(hopSize)
print(len(audio))
n = 0 
for fstart in range(0, len(audio)-frameSize, hopSize):
    n +=1 
    print(n)
    frame = audio[fstart:fstart+frameSize]
    mfcc_bands, mfcc_coeffs = mfcc(spectrum(w(frame)))
    mfccs.append(mfcc_coeffs)
    melbands.append(mfcc_bands)