'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples

pip install pyttsx3
'''

import pyttsx3

engine = pyttsx3.init()
with open("sample_text.txt", 'r') as source:
  theText = source.read()
  engine.say(theText)

engine.runAndWait()