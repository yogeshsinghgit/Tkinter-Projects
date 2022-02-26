from tkinter import *
class Calc:
	def __init__(self,master):
		self.MathVariable = 0
		self.Value = 0
		self.master = master
 
		self.NumberEntry = Entry(self.master, width=40, borderwidth=5,justify=CENTER)
		self.NumberEntry.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
		i,j=1,0
		for btn in ['1','2','3','4','5','6','7','8','9','+','-','0','*','/','=']:
			if i%4==0:
				i=1
				j+=1
			Button(self.master,text=btn, width=5,command=lambda num =btn:self.BtnClick(num)).grid(row=i, column=j,ipadx=4)
			i+=1
		self.clear = Button(self.master,text='Clear', width=15,command=self.Clear).grid(row=5, columnspan=6,ipadx=70)
 
	def BtnClick(self, number):
		if number == '=':
			self.Equal()
		else:
			self.NumberEntry.insert(len(self.NumberEntry.get()) + 1, str(number))
	def Equal(self):
		value1 = self.NumberEntry.get()
		try:
			value1 = eval(value1)
			self.NumberEntry.delete(0, END)
			self.NumberEntry.insert(0, value1)
		except Exception as e:
			self.NumberEntry.delete(0, END)
			self.NumberEntry.insert(0, e)


	def Clear(self):
		self.NumberEntry.delete(0, END)
		self.Value = 0
 
if __name__ == "__main__":
    master = Tk()
    master.title('Calculator')
    master.iconbitmap('icon.ico')
    master.geometry('272x155')
    master.resizable(0,0)
    Calc(master)
    master.mainloop()
