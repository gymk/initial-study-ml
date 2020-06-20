'''
conda install matplotlib
conda install scipy

Mono Audio Samples: http://www0.cs.ucl.ac.uk/teaching/GZ05/samples/
'''

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('mask-100-550.wav')
#sample_rate, samples = wavfile.read('..\\audio_editing\\audio.wav')
frequencies, times, spectogram = signal.spectrogram(samples, sample_rate)

plt.imshow(spectogram)
plt.ylabel('Freq (kHz)')
plt.xlabel('Time (sec)')
plt.show()
