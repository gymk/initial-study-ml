'''
conda install pyaudio

Additional Resource: https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
'''

import os
import streamlit as st
import tempfile
import pyaudio
import wave

# Create required global variables
if not hasattr(st, 'wav_tmp_file'):
  temp_name = "sr_recording_" + next(tempfile._get_candidate_names()) + '.wav'
  print(temp_name)
  st.wav_tmp_file = tempfile._get_default_tempdir() + "\\sr_recording_" + next(tempfile._get_candidate_names()) + '.wav'
  st.write(st.wav_tmp_file)

st.text('Try record, play and covert')

def recordWavAudio(wav_file_name):
  chunk = 1024  # Record in chunks of 1024 samples
  sample_format = pyaudio.paInt16  # 16 bits per sample
  channels = 2
  fs = 44100  # Record at 44100 samples per second
  seconds = 3
  filename = wav_file_name #"output.wav"

  p = pyaudio.PyAudio()  # Create an interface to PortAudio

  print(f'Recording to {wav_file_name}')

  stream = p.open(format=sample_format,
                  channels=channels,
                  rate=fs,
                  frames_per_buffer=chunk,
                  input=True)

  frames = []  # Initialize array to store frames

  # Store data in chunks for 3 seconds
  for _ in range(0, int(fs / chunk * seconds)):
      data = stream.read(chunk)
      frames.append(data)

  # Stop and close the stream 
  stream.stop_stream()
  stream.close()
  # Terminate the PortAudio interface
  p.terminate()

  print('Finished recording')

  # Save the recorded data as a WAV file
  wf = wave.open(filename, 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(p.get_sample_size(sample_format))
  wf.setframerate(fs)
  wf.writeframes(b''.join(frames))
  wf.close()
  return

def playWavAudio(wav_file_name):
  print(f'Playing {wav_file_name}')
  filename = wav_file_name #'output.wav'

  # Set chunk size of 1024 samples per data frame
  chunk = 1024  

  # Open the sound file 
  wf = wave.open(filename, 'rb')

  # Create an interface to PortAudio
  p = pyaudio.PyAudio()

  # Open a .Stream object to write the WAV file to
  # 'output = True' indicates that the sound will be played rather than recorded
  stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True)

  # Read data in chunks
  data = wf.readframes(chunk)

  # Play the sound by writing the audio data to the stream
  while data != b'':
      stream.write(data)
      data = wf.readframes(chunk)

  # Close and terminate the stream
  stream.close()
  p.terminate()
  return

def convertWavToText():
  return

def onButtonClick_RevWaveAudio():
  recordWavAudio(st.wav_tmp_file)
  return

def onButtonClick_PlayWaveAudio():
  playWavAudio(st.wav_tmp_file)
  return

def onButtonClick_ConvertWaveAudioToText():
  # To DO
  st.text('Yet to implement')
  return

if st.button('Record WAVE Audio'):
  onButtonClick_RevWaveAudio()

if st.button('Play WAVE Audio'):
  onButtonClick_PlayWaveAudio()

if st.button('Convert WAVE to Text'):
  onButtonClick_ConvertWaveAudioToText()
