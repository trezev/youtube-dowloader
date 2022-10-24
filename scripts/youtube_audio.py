import os
from pytube import YouTube
audio_get = YouTube(str(input("\n\nYOUTUBE AUDIO DOWLOADER\nurl: "))).streams.filter(only_audio=True).first().download()
base, ext = os.path.splitext(audio_get)
audio_out = base + ".mp3"
os.rename(audio_get, audio_out)