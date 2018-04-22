from pytube import YouTube,Playlist
from pprint import pprint
import sys

def downloadVideo(url):
    YouTube(url).streams.first().download('C:\Downloads')

def downloadPlaylist(playlistUrl):
     pl = Playlist(playlistUrl)
     pl.download_all('C:\Downloads')

"""
yt.set_filename(sys.argv[2])
pprint(yt.get_videos())
format=input("enter video format: ")
pixel=input("enter pixels from list: ")
video = yt.get(format,pixel)
video.download('c://Downloads');
"""
