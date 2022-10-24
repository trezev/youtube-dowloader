from pytube import YouTube
YouTube(input("\n\nYOUTUBE VIDEO DOWLOADER\nurl: ")).streams.get_highest_resolution().download()