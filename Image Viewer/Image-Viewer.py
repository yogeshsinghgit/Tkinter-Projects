# Github : yogeshsinghgit
# follow me on Github..
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog
import os
 
 
class ImageView:
 
	def __init__(self,root):
		self.root = root
		self.root.title("Image-Viewer")
		self.root.geometry('850x530')
		self.root.resizable(0,0)
 
		# important things ....
		self.i = 0
		# image list
		self.Image_list = []
		# current path you can use here your default path ok bro ....
		self.path =""
		# possible extensions of images
		self.extension = ['JPG','BMP','PNG']
 
		# create canvas ...
		self.canvas = Canvas(self.root,bd=5,relief=RIDGE)
		self.canvas.place(x=0,y=0,height=500,width=850)
 
		# create buttons
 
		self.previous_button = Button(self.root,text="<",width=3,font=('arial',10,'bold'),command=self.previous_image)
		self.previous_button.place(x=360,y=500)
 
		self.next_button = Button(self.root,text=">",width=3,font=('arial',10,'bold'),command=self.next_image)
		self.next_button.place(x=455,y=500)
 
 
		self.open_button = Button(self.root,text="Open",width=5,font=('arial',10,'bold'),command=self.open_file)
		self.open_button.place(x=400,y=500)
 
	# open function .....
	def open_file(self):
		self.path = filedialog.askdirectory()
		if self.path:
			self.Image_list = []
			self.add_image()
 
 
 
	def add_image(self):
		for image in os.listdir(self.path):
			ext = image.split('.')[::-1][0].upper()
			if ext in self.extension:
				self.Image_list.append(image)
 
		self.resize(self.Image_list[0])
 
		# resize function
	def resize(self,image):
		if self.path :
			os.chdir(self.path)
			image_p = self.path + '\\' + str(image)
			img = PIL.Image.open(image)
			# img.show()
			width, height = img.size
			if (int(width) > 850 and int(height) < 500):
				img = img.resize((850, height))
			elif (int(height) > 500 and int(width) < 850):
				img = img.resize((width, 500))
			elif (int(width) > 850 and int(height) > 500):
				img = img.resize((840, 480))
 
			storeobj = ImageTk.PhotoImage(img)
			self.canvas.delete(self.canvas.find_withtag("bacl"))
			w = self.canvas.winfo_width()
			h = self.canvas.winfo_height()
			self.canvas.image = storeobj  # <--- keep reference of your image
			self.canvas.create_image(w / 2, h / 2, image=storeobj, anchor=CENTER)
 
			# print(self.canvas.find_withtag("bacl"))
			self.root.title("Image Viewer ({})".format(image_p))
 
	def next_image(self):
		self.i+=1
		try:
			self.image = self.Image_list[self.i]
			self.resize(self.image)
		except:
			pass
 
	def previous_image(self):
		self.i -=1
		try:
			self.image = self.Image_list[self.i]
			self.resize(self.image)
		except:
			self.i = 1
 
 
if __name__ == '__main__':
	root = Tk()
	img = ImageView(root)
	root.mainloop()
