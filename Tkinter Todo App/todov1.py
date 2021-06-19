# To Do Application Using File Handling
import tkinter as tk

task_list = []

def addTask(*args):
    task = task_entry.get()
    task_entry.delete(0,tk.END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END,task)

def deleteTask(*args):
    global task_list
    task = str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(tk.ANCHOR)

    
def openTaskFile():
    global task_list
    with open("tasklist.txt",'r') as taskfile:
        tasks = taskfile.readlines()
    for task in tasks:
        if task !='\n':
            task_list.append(task)
            listbox.insert(tk.END,task)
    

root = tk.Tk()
root.title("To Do App")
root.geometry("300x360")
root.config(bg="#8400ff")

frame = tk.Frame(root,bd=3,width=300,height=280)
frame.pack(pady=10)


listbox = tk.Listbox(frame,font=('arial',12),width=28,height=12)
listbox.pack(side=tk.LEFT,fill=tk.BOTH,padx=2)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# read The Task File and insert the task in listbox/tasklist
openTaskFile()

task_entry = tk.Entry(root,width=20,font=('times',14))
task_entry.pack(pady=10)
task_entry.bind("<Return>",addTask)

btn_frame = tk.Frame(root,width=280,height=5)
btn_frame.pack(pady=10)

add_task_btn = tk.Button(btn_frame,text="Add Task",bg='light green',command=addTask)
add_task_btn.grid(row=0,column=0)

del_task_btn = tk.Button(btn_frame,text="Delete Task",bg='#e20049',command=deleteTask)
del_task_btn.grid(row=0,column=1)

root.mainloop()
