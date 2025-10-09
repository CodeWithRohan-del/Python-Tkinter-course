
# -----------------------Buutons and checkbuttons -----------------

#importing Tkinter
import tkinter as tk

#create a Tk() class object
root= tk.Tk()

#create a Label to display Text
label = tk.Label(text="Welcome to Button app",bg="#200505",font=("Arial",17,"bold"))
label.pack()

root.geometry("800x500")
#create  a buttons
#To create buttons using tk.Button class 
#create  a four buttons
#text= you want your text
# add command to work command= your fuction
#create a fuction for button
def printhello():
    print("Hello I am Rohan")
button_1 = tk.Button(root,text="First button",command=printhello).pack()


#cretae a Check buttons 
check = tk.Checkbutton(text="check here..") #return 1 ,0
check.pack()
#run the mainloop
root.mainloop()

#-----------------program Ready  -----------------