'''
https://medium.com/@patrickbfuller/librosa-a-python-audio-libary-60014eeaccfb

conda install -c conda-forge librosa
'''

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
#data, sample_rate = librosa.load('../audio_editing/audio.wav')
data, sample_rate = librosa.load('../speech-to-text/male.wav')

print(f'data.shape: {data.shape} SampleRate: {sample_rate}')

# Display Power Spectrogram (amplitude squared)
spec = librosa.feature.melspectrogram(y=data, sr=sample_rate)
librosa.display.specshow(spec, y_axis='mel', x_axis='s', sr=sample_rate)
plt.colorbar()
plt.show()

# Convert amplitude squared to decibels and then display
db_spec = librosa.power_to_db(spec, ref=np.max)
librosa.display.specshow(db_spec, y_axis='mel', x_axis='s', sr=sample_rate)
plt.colorbar()
plt.show()
