from pytube import YouTube
from pprint import pprint
import sys

yt = YouTube(sys.argv[1])
yt.set_filename(sys.argv[2])
pprint(yt.get_videos())
format=input("enter video format: ")
pixel=input("enter pixels from list: ")
video = yt.get(format,pixel)

video.download('c://Downloads');
