
#-------------  Add Scroll bar in Tkionter --------------

#importing tkinter
import tkinter as tk

#import tkk class in tkinter
from tkinter import ttk

#create a root object
root = tk.Tk()

#Set window size
root.geometry("1000x600")

#set window title
root.title("Scroll Bar")

#create Frame for scrool bar
frame = ttk.Frame(root)
frame.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)


#craete a scroll bar
scrollbar = ttk.Scrollbar(frame,orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

#Add list for Scroll bar 
listbox = tk.Listbox(frame,width=40,height=10,yscrollcommand=scrollbar.set)

#Insert list itmes 
for i in range(300):
    listbox.insert(tk.END,f"{i}")


#pack the list box 
listbox.pack(pady=10,side=tk.LEFT,fill=tk.BOTH,expand=True)

#Run mainloop
root.mainloop()