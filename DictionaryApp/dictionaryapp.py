import tkinter as tk
from tkinter import ttk
from PyDictionary import PyDictionary
# pip install pydictionary

def result(*args):
    word = text_entry.get()
    if word:
        try:
            dict = PyDictionary()
            mean_dict = dict.meaning(word)
        except exception as e:
            mean_dict=None
            label3['text'] ='Error : \n'+str(e)
            
        if mean_dict:
            label1['text'] = word.capitalize()
            label2['text'] = "/".join(list(mean_dict.keys()))

            meaning_string = ''
            line_counter =0
            for meanings in list(mean_dict.values())[0]:
                if len(meaning_string)<200:
                    line_counter+=1
                    s = meaning_string
                    meaning_string+=meanings.capitalize()+".\n"
                if line_counter==3:
                    break
            label3['text'] = s
            label3.config(fg='#000000')
        else:
            label1['text'] = word.capitalize()
            label2['text'] = "No Such Word"
            label3.config(fg='red')
            label3['text'] = f"we can't find any match for word =>\n\"{word}\""


        
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
root = tk.Tk()
s= ttk.Style(root)
s.theme_use('xpnative')
root.title("Python Dictionary")
root.resizable(0,0)
root.geometry("300x200")
root.config(bg='white')

text_entry = ttk.Entry(root,width=20,font=("Sitka Small",11),justify=tk.CENTER)
text_entry.bind("<Return>",result)
text_entry.place(x=10,y=21)

search_btn = tk.Button(root,text="Search",bg='#8c52ff',fg='#ffffff',font=("Sitka Small",9),
        width=7,relief=tk.FLAT,command=result)
search_btn.place(x=220,y=20)

output_frame = tk.Frame(root,bg='#ffffff')
output_frame.place(x=10,y=70,height=120,width=280)

label1 = tk.Label(output_frame,font=("Arial",12,'bold'),bg='#ffffff')
label1.place(x=10,y=5)

label2 = tk.Label(output_frame,font=("Sitka Small",6,'italic'),justify=tk.LEFT,fg='#a6a6a6',bg='#ffffff')
label2.place(x=10,y=30)

label3 =  tk.Message(output_frame,width=250,font=("Sitka Small",8),
            bg='#ffffff',justify=tk.LEFT)
label3.place(x=10,y=45)


root.mainloop()
