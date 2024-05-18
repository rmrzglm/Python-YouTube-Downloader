from pytube import YouTube

def video_download(url, path='/home/Victor Reyes/Videos'):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        print("Download Complete!")
    except Exception as e:
        print("Error!", e)

def audio_download(url, path = '/home/Victor Reyes/Music'):
    try:
        yt = YouTube(url)
        yt.streams.get_audio_only().download(output_path=path)
        print("Audio Download Complete!")
    except Exception as e:
        print ("Error!", e)

url_yt = input("Give the URL YT: ")
path = input("Give the path or use default: ")
v_ao = input("Do you want the full video or only the audio? ")
vd_a = v_ao.title()

if vd_a == "Video":
    video_download(url_yt, path)
elif vd_a == "Audio":
    audio_download(url_yt, path)
else:
    print ("The option that you chose isn't aviable!")