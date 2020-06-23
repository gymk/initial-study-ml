'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples

Install Guide: https://www.codesofinterest.com/2017/03/python-speech-recognition-pocketsphinx.html
conda install swig # https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed
pip install pocketsphinx

MSVC Error: https://github.com/benfred/implicit/issues/76

New Inst: http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/
'''

import speech_recognition as sr
from os import path
AUDIO_FILE = "male.wav"

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
  audio = r.record(source)

try:
  print("Sphinx thinks you said " + r.recognize_sphinx(audio, language='en-us'))
except sr.UnknownValueError:
  print("Sphinx could not understand audio")
except sr.RequestError as e:
  print(f"Sphinx error; {e}")
