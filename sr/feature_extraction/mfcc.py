'''
pip install python_speech_features
'''

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

(samplerates, signal) = wav.read('mask-100-550.wav')
mfccfeatures = mfcc(signal, samplerates)
dmfccfeature = delta(mfccfeatures, 2)
fbankfeature = logfbank(signal, samplerates)

print(fbankfeature)

'''
Output:

WARNING:root:frame length (1200) is greater than FFT size (512), frame will be truncated. Increase NFFT to avoid.
WARNING:root:frame length (1200) is greater than FFT size (512), frame will be truncated. Increase NFFT to avoid.
[[-36.04365339 -36.04365339 -36.04365339 ... -36.04365339 -36.04365339
  -36.04365339]
 [-36.04365339 -36.04365339 -36.04365339 ... -36.04365339 -36.04365339
  -36.04365339]
 [-36.04365339 -36.04365339 -36.04365339 ... -36.04365339 -36.04365339
  -36.04365339]
 ...
 [ 16.38801634  11.4647145   10.5526182  ...   4.76865241   4.8273502
    5.02387089]
 [ 16.39915529  11.32660613  10.11817974 ...   5.65919987   5.6341599
    5.67122076]
 [ 16.38801634  11.4647145   10.5526182  ...   4.76865241   4.8273502
    5.02387089]]
'''