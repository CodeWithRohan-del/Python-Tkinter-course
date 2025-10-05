
#----------------------Display Image in Tkinter Window 

#Imaporting Tkinter
import tkinter as tk

#Imaporting pillow module to display jpg image
from PIL import Image,ImageTk

#Create a root object
root = tk.Tk()

#Display PNG image

#png image for use tk.PhotoImage(pass the your image  path)
photo = tk.PhotoImage(file="laptop.png")

#create Lable to Display png Image
png = tk.Label(image=photo)
png.pack()

#For JPG image
#open the jpg image
open_image = Image.open("Jpg image.jpg")

#pass the tk.PhotoImage 
photo_1 = ImageTk.PhotoImage(open_image)

#Create a Label to Display JPG image
jpg = tk.Label(image=photo_1)
#jpg.pack()

#Run the mainloop
root.mainloop()

#--------------program is Ready -------------------------------------