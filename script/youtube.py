import os
from pytube import YouTube
ver = int(input("\n1 - MP4\n2 - MP3\n"))
if ver == 1:
    video_get = YouTube(input("\n\nYOUTUBE VIDEO DOWLOADER\nurl: ")).streams.get_highest_resolution().download()
    base, ext = os.path.splitext(video_get)
    os.startfile(video_get)
    input("\n\nSuccessfully downloaded\n\n")
elif ver == 2:
    audio_get = YouTube(str(input("\n\nYOUTUBE AUDIO DOWLOADER\nurl: "))).streams.filter(only_audio=True).first().download()
    base, ext = os.path.splitext(audio_get)
    audio_out = base + ".mp3"
    os.rename(audio_get, audio_out)
    os.startfile(audio_out)
    input("\n\nSuccessfully downloaded\n\n")
else:
    input("3rr0r")
    