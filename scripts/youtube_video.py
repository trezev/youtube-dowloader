from pytube import YouTube # to install pytube: python -m pip install pytube
YouTube(input("\n\nYOUTUBE VIDEO DOWLOADER\nurl: ")).streams.get_highest_resolution().download() # the file will be saved in the folder where the script is located
print("\n\nSuccessfully downloaded\n\n") # print "Successfully downloaded" when file dowloaded