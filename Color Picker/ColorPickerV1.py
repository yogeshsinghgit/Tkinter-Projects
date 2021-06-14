# >> @dynamic.coding <<


"""
Python Tkinter Color Picker to choose color in Hex and RGB Format ...
"""
import tkinter as tk
from tkinter import Entry, Frame, Label
from tkinter.constants import  HORIZONTAL, RAISED, SUNKEN

class Colorpicker:
    def __init__(self,root):
        self.root = root
        self.root.title("Color Picker")
        self.root.geometry("300x420")
        self.root.resizable(0,0)

        self.R = tk.IntVar()
        self.G = tk.IntVar()
        self.B = tk.IntVar()
        self.hex = tk.IntVar()




        self.color_canvas = Label(self.root,bg="#8400ff",width=40,height=10,bd=2,relief=RAISED)
        self.color_canvas.place(x=7,y=2)
        self.color_canvas.bind("<Double-1>",self.copy_color)

        frame = Frame(self.root,bd=2,relief=SUNKEN)
        frame.place(x=7,y=170,height=180,width=285)

        r_label = Label(frame,text="R",width=5,fg="#ff0000",font=('arial',10,'bold'))
        r_label.place(x=5,y=24)

        self.R_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#ff0000"
        ,orient=HORIZONTAL,command=self.scaleMove)
        self.R_Scale.set(132)
        self.R_Scale.place(x=40,y=6)

        g_label = Label(frame,text="G",width=5,fg="#00a200",font=('arial',10,'bold'))
        g_label.place(x=5,y=68)

        self.G_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#00a200"
        ,orient=HORIZONTAL,command=self.scaleMove)
        self.G_Scale.place(x=40,y=50)

        b_label = Label(frame,text="B",width=5,fg="#0000ff",font=('arial',10,'bold'))
        b_label.place(x=5,y=122)

        self.B_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#0000ff"
        ,orient=HORIZONTAL,command=self.scaleMove)
        self.B_Scale.set(255)
        self.B_Scale.place(x=40,y=105)

        hex_label = Label(self.root,text="Hex Code :",font=('arial',10,'bold'))
        hex_label.place(x=7,y=360)

        self.hex_entry = Entry(self.root,width=12,font=('arial',10))
        self.hex_entry.insert(tk.END,'##8400ff')
        self.hex_entry.place(x=90,y=360)

        rbg_label = Label(self.root,text="RGB Code :",font=('arial',10,'bold'))
        rbg_label.place(x=7,y=390)

        self.rgb_entry = Entry(self.root,width=12,font=('arial',10))
        self.rgb_entry.place(x=90,y=390)

    def scaleMove(self,*args):
        self.R = int(self.R_Scale.get())
        self.G = int(self.G_Scale.get())
        self.B = int(self.B_Scale.get())
        rgb = f"{self.R},{self.G},{self.B}"

        #print(r,g,b)
        self.hex =  "#%02x%02X%02x"%(self.R,self.G,self.B)
        self.color_canvas.config(bg=self.hex)
        # Hex to RGB
        #h = color_hex.lstrip('#')
        #print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

        self.hex_entry.delete(0,tk.END)
        self.hex_entry.insert(0,self.hex)

        self.rgb_entry.delete(0,tk.END)
        self.rgb_entry.insert(0,rgb)

    
    def copy_color(self,*args):
        root.clipboard_clear()  # clear clipboard contents
        root.clipboard_append(self.hex)  # append new value to clipbaord
        


root = tk.Tk()
Colorpicker(root)
root.mainloop()
