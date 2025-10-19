

#-----------Set window Background Color In Tkinter -------

#importing Tkinter 
import tkinter as tk 

# create a root object 
root =  tk.Tk()

#set the window size 
root.geometry("900x700")

#set the window color --> configure bg="your color name" as string
root.configure(bg="#383E06") #treck

#Run the mainloop
root.mainloop()