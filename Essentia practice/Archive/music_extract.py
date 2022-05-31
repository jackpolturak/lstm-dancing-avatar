import essentia
import essentia.standard as es



# Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                              rhythmStats=['mean', 'stdev'],
                                              tonalStats=['mean', 'stdev'])('/Users/jackpolturak/Documents/Design Engineering/DES4/Master Thesis /Post Easter/Essentia practice/Drums.wav')

# See all feature names in the pool in a sorted order
print(sorted(features.descriptorNames()))

# print("Filename:", features['metadata.tags.file_name'])
print("-"*80)
print("SPECTRQL ENERGY:", features_frames['rhythm.bpm'])
print("EBU128 integrated loudness:", features['lowlevel.loudness_ebu128.integrated'])
# print("EBU128 loudness range:", features['lowlevel.loudness_ebu128.loudness_range'])
# print("-"*80)
# print("MFCC mean:", features['lowlevel.mfcc.mean'])
# print("-"*80)
# print("BPM:", features['rhythm.bpm'])
# print("Beat positions (sec.)", features['rhythm.beats_position'])
# print("-"*80)
# print("Key/scale estimation (using a profile specifically suited for electronic music):",
#       features['tonal.key_edma.key'], features['tonal.key_edma.scale'])



# print(features_frames)