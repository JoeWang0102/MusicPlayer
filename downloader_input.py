from pytube import YouTube
import os
from env import userParameters as Param
url = input("下載網址:")
file_name = ''
try:
    yt = YouTube(url)
    print(yt.title)
    file_name = yt.title.replace('.','').replace('/','').replace('\\','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','').replace(':','').replace(' ','').replace('&','and')
    yt.streams.filter(type="audio").order_by('abr').first().download(output_path=Param.musicPath, filename='audio.mp4')
    yt.streams.filter(type="video").first().download(output_path=Param.musicPath, filename='video.mp4')
    os.chdir(Param.musicPath)
    # os.system('ffmpeg -i video.mp4 -i audio.mp4 -map 0:v -map 1:a -c copy -y %s.mp4'%(file_name))
    # os.system('ffmpeg -i %s.mp4 %s.mp3'%(file_name,file_name))
    # os.remove('video.mp4')
    # os.remove('audio.mp4')
    # os.remove(file_name+'.mp4')
    # new_name = file_name.replace('and','&')
    # os.rename(file_name+'.mp3',new_name+'.mp3')
    print(file_name,'\ndownload finish')
except Exception as e:
    print('#-----------------#')
    print(e)
    print("Video download failed")
    print('#-----------------#')
