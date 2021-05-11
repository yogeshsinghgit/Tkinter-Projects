# Github : yogeshsinghgit
# make sure to follow me on Github ...

from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
 
 
class Pynote:
    def __init__(self,root):
        self.root = root
        
        self.filename = None
 
        # create menu bar ..
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save as...", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)
 
        self.textarea = ScrolledText(self.root,font=('arial', 14),undo=True,wrap = WORD)
        self.textarea.place(relwidth=1, relheight=1)
 
 
    # methods ......
 
    def new_file(self, *args):
        self.textarea.delete(1.0, END)
        self.filename = None
 
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
 
 
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0,END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                messagebox.showerror("Pynote Says",e)
        else:
            self.save_as()
 
    def save_as(self, *args):
        try:
            self.filename = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])
            textarea_content = self.textarea.get(1.0,END)
            with open(self.filename, "w") as f:
                f.write(textarea_content)
        except Exception as e:
            messagebox.showerror("Pynote Says",e)
 
 
if __name__ == "__main__":
    root = Tk()
    root.title("Pynote -Dynamic Coding")
    root.geometry('500x500')
    Pynote(root)
    root.mainloop()
