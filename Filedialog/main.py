

#-----------------Filedilog In Tkinter------------------

#Filedilog to use the File mangement Task For Example 
# file open
# file create And so on.


#importing Tkinter
import tkinter as tk

#Importing filedilog  
from tkinter import filedialog

from PIL import Image,ImageTk
#Create a root  object 
root = tk.Tk()

#Set window size 
root.geometry("800x600")


#Functions 

#--------------Open file and Folder Function --------------
#Open file 
def openfile():
    d = filedialog.askopenfile(typevariable=".jpg",var=openfiles)

def openfolder():
    filedialog.askdirectory()

#-----------------Save and Save as Function ---------------

openfiles
#Save function 
def save():
    filedialog.asksaveasfilename()

#Saveas function 
def saveas():
    filedialog.asksaveasfile()





#images 
photo = Image.open(f"{}")

#
def demo():

#Create a button 
button = tk.Button(text="open",command=demo).pack(anchor="center")

#create a label for show images 
label = tk.Label(image=photo)

#Run mainloop
root.mainloop()