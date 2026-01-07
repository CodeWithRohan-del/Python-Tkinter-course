
#-----------------OpenDicretory Functon --------------

# Importing Tkinter
import tkinter as tk

#import filedialog form Tkinter
from tkinter import filedialog

#create a root object 
root = tk.Tk()

#Set window size 
root.geometry("800x500")

# Open Dirctory function 
 # To return path the of selected Dir.
 # Arguments 
  #Title 

def openfolder():
    path = filedialog.askdirectory(title="Open folder")

    if path:
        display.config(text=f"Selected Folder: {path}")

button = tk.Button(root,text="Openfile",command=openfolder).pack(anchor="center")

#create a label
display = tk.Label(root, text="No file selected", font=("Arial", 10))
display.pack(pady=10)

#Run the mainloop
root.mainloop()
