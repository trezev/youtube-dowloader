from pytube import YouTube
url = str(input("\nurl: "))
slc_res = input("\n\nSelect video resolution:\n0 - highest resolution\n1 - 144p\n2 - 240p\n3 - 360p\n4 - 480p\n5 - 720p\n6 - 1080p\n :")
if slc_res == "0":
    YouTube((str(url))).streams.get_highest_resolution().download()
if slc_res == "1":
    YouTube((str(url))).streams.filter(res="144p").first().download()
if slc_res == "2":
    YouTube((str(url))).streams.filter(res="240p").first().download()
if slc_res == "3":
    YouTube((str(url))).streams.filter(res="360p").first().download()
if slc_res == "4":
    YouTube((str(url))).streams.filter(res="480p").first().download()
if slc_res == "5":
    YouTube((str(url))).streams.filter(res="720p").first().download()
if slc_res == "6":
    YouTube((str(url))).streams.filter(res="1080p").first().download()
print("\n\nSuccessfully downloaded video file\n\n")
# i will do it more greater...