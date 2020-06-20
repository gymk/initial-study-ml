'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples
'''

import speech_recognition as sr
from os import path
AUDIO_FILE = "male.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
  audio = r.record(source)

try:
  print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
  print("Sphinx could not understand audio")
except sr.RequestError as e:
  print(f"Sphinx error; {e}")
