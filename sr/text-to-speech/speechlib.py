'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples

conda install comtypes
'''

from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib
infile = 'sample_text.txt'
outfile = 'sample_text.wav'
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
f = open(infile, 'r')
theText = f.read()
f.close()
engine.speak(theText)
stream.Close()