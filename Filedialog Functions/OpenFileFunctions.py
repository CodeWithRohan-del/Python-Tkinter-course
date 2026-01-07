
#------------------Open Files Function ---------------

#Function open files
# 1. askopen file 
# 2. askopenfilename 
# 3 askopenfilenames

# Importing Tkinter
import tkinter as tk

#import filedialog form Tkinter
from tkinter import filedialog

#create a root object 
root = tk.Tk()

#Set window size 
root.geometry("800x500")

#Openfile Function 
# --> Openfile Function to open the file.
 # Arguments 
  # 1. title ,2.Mode , 3. Filetypes 

def openfile():
    path = filedialog.askopenfile(title="OpenFile",mode="r",filetypes=(("Python file","*py"),("Text File","*.txt")))
    print(path)
    #use path To other create programs.



# --> Askopenfilename 
    #Arguments
     # 1.Title , 2. Filetypes 
     #openfilename function to use retun path of file
def openfilename():
    path_1 = filedialog.askopenfilename(
        title="OpenfileName",filetypes=(("Python File","*.py"),("All files","*.*"))
    )
    if path_1:
        display.config(text=f"Selected path: {path_1}")

# Askopenfilenames function 
 # openfilenames function return file path as a tuple
  #Arguments 
   # same open filename

def openfilenames():
    path_2 = filedialog.askopenfilenames(
        title="OpenfileName",filetypes=(("Python File","*.py"),("All files","*.*"))
    )
    if path_2:
        display.config(text=f"Selected path: {path_2}")


button = tk.Button(root,text="Openfile",command=openfilenames).pack(anchor="center")

#Create a label to display the path on window 
display = tk.Label(root, text="No file selected", font=("Arial", 10))
display.pack(pady=10)

#Run the mainloop
root.mainloop()

#-------------------Thius is Open file Functions ------------------
