# Github >> yogeshsinghgit <<< 
# Follow me on Instagram @dynamic.coding 


from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess, os
from tkinter import messagebox
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator

compiler = Tk()
compiler.title('PyCode - Dynamic Coding')
file_path = ''



def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    # print("Open Path",path)
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        messagebox.showwarning("Pycode Warning",'Please save your code')
        return
    file_name =  os.path.basename(file_path)
    #print(f"File Name  : {file_name}")
    command = f'python {file_name}'
    #print("command :",command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # print("Output : ",output)
    # print("Error : ",error)
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
Percolator(editor).insertfilter(ColorDelegator())

code_output = Text(height=10,fg='blue')
code_output.pack()

compiler.mainloop()
