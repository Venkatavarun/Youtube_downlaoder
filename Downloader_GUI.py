#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from pprint import pprint



def getVideos():
	cur_entry = url.get()
	pprint(cur_entry)
	yt = YouTube(cur_entry)
	pprint(yt)
	return;
def download():
    pprint(Format)
    return;

root = Tk()
root.title('Youtube Downlaoder')
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

url = StringVar()
Format = StringVar()
lst = [1,2,3]

ttk.Label(mainframe, text='URL').grid(column=1, row=1, sticky=W)
urlEntry = ttk.Entry(mainframe, width=7, textvariable=url)
urlEntry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text='available Format').grid(column=1, row=2,sticky=W)

optMenu = OptionMenu(mainframe, Format, *lst).grid(column=2, row=2,sticky=(W, E))

ttk.Button(mainframe, text='Download',command=download).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

urlEntry.bind("<FocusOut>",getVideos)

root.mainloop()
