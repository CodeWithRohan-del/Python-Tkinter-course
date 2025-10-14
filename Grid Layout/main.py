
#-----------------grid layout In Tkinter -----------
#grid layout use to pack the Attributs on row and column wise

#------------start write code -------------
#importing Tkinter 
import tkinter as tk

#create a Tk() class root objects
root = tk.Tk()

#set a window size
root.geometry("800x400")

#create Label and pack the use of grid Layout
welcome = tk.Label(text="Welcome to GUI",font=("Arial",16,"bold")).grid(row=0,column=1)
#grid layout get to Argumets row= and column= 

#create a to label name and age create a Entry on the label 
name  = tk.Label(text="Name").grid(row=1,column=0)
age = tk.Label(text="Age").grid(row=2,column=0)

#create a text vriable for Entryes 
namevar = tk.StringVar() 
agevar = tk.StringVar()

#create a Entry
name_Entry = tk.Entry(root,textvariable=namevar).grid(row=1,column=1)
age_Entry = tk.Entry(root,textvariable=agevar).grid(row=2,column=1)

#create a Function for Sumbit Buttons
def sumbit():
    print("Form is Sumbited by GUI ")

#create a buttons and pass the command 
button = tk.Button(root,text="Sumbit",command=sumbit).grid(row=3,column=1)

#Run The mainloop()
root.mainloop()

#---------------This is the grid layout------------------