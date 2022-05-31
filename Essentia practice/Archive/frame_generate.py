import essentia
import essentia.standard as es
from essentia.standard import *
from matplotlib.pyplot import bar
import numpy as np
import pandas as pd 
from math import *

audio_file = '/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Essentia practice/Drums.wav'
print("-"*80)
print(dir(essentia.standard))

audio = es.MonoLoader(filename=audio_file)()
windowing = es.Windowing(type='hann', zeroPadding=2048)
spectrum = es.Spectrum()
melbands = es.MelBands(numberBands=96, lowFrequencyBound=0, highFrequencyBound=11000)
spectrum_logfreq = es.LogSpectrum(binsPerSemitone=1)



barkbands = es.BarkBands()
pitchSAL = es.PitchSalience()

print("-"*80)
print(dir(essentia.standard))

amp2db = es.UnaryOperator(type='lin2db', scale=2)
pool = essentia.Pool()



sample_rate = 44100

hopsize = int(sample_rate/28)

print(hopsize)





barkbankd = []
pitch = []
#1024

n = 0
for frame in es.FrameGenerator(audio, frameSize=1024, hopSize=hopsize):
    n += 1
    frame_spectrum = spectrum(windowing(frame))
    frame_mel = melbands(frame_spectrum)
    frame_spectrum_logfreq, _, _ = spectrum_logfreq(frame_spectrum)
    

    #HERE COME UP WITH EVER~YTHING U NEED 
    frame_barkbands = barkbands(frame_spectrum)
    frame_pitch = pitchSAL(frame_spectrum)
    energy_band = energy_band(frame_spectrum)


    barkbankd.append(frame_barkbands)
    pitch.append(frame_pitch)
    print((frame_pitch), n)
    pool.add('spectrum_db', amp2db(frame_spectrum))
    pool.add('mel96_db', amp2db(frame_mel))
    pool.add('spectrum_logfreq_db', amp2db(frame_spectrum_logfreq))



barkbankd = np.array(barkbankd)
df = pd.DataFrame(barkbankd)

pitch = np.array(pitch)
df_pitch = pd.DataFrame(pitch)

# print(df)
# print(df_pitch)



