import tkinter as tk
from tkinter import ttk, filedialog
import os
from pygame import mixer # pip install pygame

def play_song():
    mixer.music.load(playlist.get(tk.ACTIVE))
    mixer.music.play()

def set_vol(val):
    mixer.music.set_volume(float(val)/100)

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


root = tk.Tk()
mixer.init()
root.geometry("300x160")
root.title("Mini Music Player")
root.configure(bg='white')
s = ttk.Style(root)
s.theme_use('vista')

# Buttons ...
ttk.Button(root,text='Play',width=10,command=play_song()).place(x=10,y=10)
ttk.Button(root,text='Stop',width=10,command=mixer.music.stop).place(x=10,y=40)
ttk.Button(root,text='Pause',width=10,command=mixer.music.pause).place(x=10,y=70)
ttk.Button(root,text='UnPause',width=10,command=mixer.music.unpause).place(x=10,y=100)
ttk.Button(root,text='Open',width=10,command=open_folder).place(x=10,y=130)

music_frame = tk.Frame(root,bd=2,relief=tk.RIDGE)
music_frame.place(x=90,y=10,width=200,height=110)

scroll = ttk.Scrollbar(music_frame)
playlist = tk.Listbox(music_frame,width=29,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
playlist.pack(side=tk.LEFT,fill=tk.BOTH)

vol = ttk.Scale(root,from_=0,to_=100,length=180,command=set_vol)
vol.set(50)
vol.place(x=100,y=130)


root.mainloop()
