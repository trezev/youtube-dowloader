import os # for work with files
from pytube import YouTube # to install pytube: python -m pip install pytube
audio_get = YouTube(str(input("\n\nYOUTUBE AUDIO DOWLOADER\nurl: "))).streams.filter(only_audio=True).first().download() # the file will be saved in the folder where the script is located
base, ext = os.path.splitext(audio_get) # get file name
audio_out = base + ".mp3" # get original file name + mp3
os.rename(audio_get, audio_out) # rename the audio_get to audio_out