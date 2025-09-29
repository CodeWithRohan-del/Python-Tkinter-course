
#----------------------------Set the window icon and title ----------------------

#importing tkinter module
import tkinter as tk 

#importing pillow modulw for Handing the jpg images
from PIL import Image,ImageTk

#create a  tk() class object
root = tk.Tk()

#set the window size 
root.geometry("800x500")

#window title

#Title is the title of the tkinter window 
root.title("My GUI")#you pass the your title

#Set the icon photo for .png file
#image = tk.PhotoImage(file="your file name ")
#root.iconphoto(True,image)

#for jpg images 
jpg_open = Image.open("ICON.jpg")#pass your file name 
pass_image = ImageTk.PhotoImage(jpg_open)

#set icon 
root.iconphoto(True,pass_image)

#run the mainloop
root.mainloop()