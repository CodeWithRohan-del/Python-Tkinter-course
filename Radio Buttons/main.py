 #----------------------Radio Buttons In Tkinter -------------------------

#Importing Tkinter
import tkinter as tk 

#import message box from tk
from tkinter import messagebox

#create a root object
root = tk.Tk()

#set window size 
root.geometry("800x500")




#Create a Label
label = tk.Label(root,text="You are:",font=("Arial",19,"bold")).pack(anchor="w")

#createa text Variable 
var = tk.StringVar()
var.set("Radio")


#Create a Sumbit Function  
def sumbit():
    messagebox.showinfo(f"Sumbit by Harry",f"Your choice is {var.get()}")

#createa Radio Buttons 
radio = tk.Radiobutton(root,text="python developer",variable=var,value="python programmer").pack(anchor="w")
radio = tk.Radiobutton(root,text="website  developer",variable=var,value="Webite devloper").pack(anchor="w")
radio = tk.Radiobutton(root,text="mobile developer",variable=var,value="Mobile devloper").pack(anchor="w")
radio = tk.Radiobutton(root,text="app developer",variable=var,value="app developer").pack(anchor="w")
radio = tk.Radiobutton(root,text="software developer",variable=var,value="software developer").pack(anchor="w")

#create a Button
button =tk. Button(root,text="Sumbit",command=sumbit).pack(anchor="w")
#Run Mainloop
root.mainloop()