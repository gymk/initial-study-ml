'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples

conda install -c anaconda pywin322
'''

from win32com.client import constants, Dispatch
with open("sample_text.txt", 'r') as source:
  theText = source.read()
  speaker = Dispatch("SAPI.SpVoice") # Create SAPI SpVoice object
  speaker.Speak(theText)                 # Process TTS
del speaker