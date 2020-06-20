'''
Book: Deep Learning with Applications Using Python : Chatbots and Face, Object, and Speech Recognition With TensorFlow and Keras
Audio Samples: https://www.signalogic.com/index.pl?page=speech_codec_wav_samples

https://github.com/Apress/Deep-Learning-Apps-Using-Python

'''

import wave
import sys
import os
import csv

origAudio = wave.open('audio.wav', 'r')
framerate = origAudio.getframerate()
nChannels = origAudio.getnchannels()
sampWidth = origAudio.getsampwidth()
nFrames   = origAudio.getnframes()

print(f'framerate {framerate}, nChannels {nChannels}, sampWWid {sampWidth}, nFrames {nFrames}')

'''
# TO DO
filename = 'results1.csv'

exampleFile = open(filename)
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

count = 0

'''