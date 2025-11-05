
#-----------------Message Box in Tkinter ---------------------

#importing Tkinter and message box
import tkinter as tk
from tkinter import messagebox

#Create a root object
root = tk.Tk()

#set window size 
root.geometry("800x500")

#set window title
root.title("Message Box ")

#set background color
#root.configure(bg="#757272")

#create a Label
mes = tk.Label(root,text="Message Box In Tkinter",font=("Arial",16,"bold")).grid(row=0,column=2)

#create a class vriable for entry
name_var = tk.StringVar()
int= tk.IntVar()

#create a Label name a phone number
name = tk.Label(root,text="Name").grid(row=2,column=1)
phone  =  tk.Label(root,text="Phone Number").grid(row=3,column=1)

#Create Entey
name_entry = tk.Entry(root,textvariable=name_var).grid(row=2,column=2)
phone_entry =tk.Entry(root,textvariable=int).grid(row=3,column=2)

#create4 sumbit fuction 
def sumbit1():
    #add a message box showinfo
    messagebox.showinfo("Showinfo message box","Form sumbet by harry ")#title,message disply
def sumbit2():
    #show warining
    messagebox.showwarning("showwsring Message box","Invlaid phone number")#title,message disply

def sumbit3():
    #showerrror
    messagebox.showerror("ShowError Message box","no module name python..")#title,message disply

def sumbit4():

    messagebox.askquestion("ask Question ","Harry is a Noun")#title,message disply

def sumbit5():
    messagebox.askokcancel("ask OK Cancel","You are Sumbited form by Hrry")#title,message disply

def sumbit6():
    messagebox.askretrycancel("ask retry cancel","downloading files ")#title,message disply
    
def sumbit7():
    messagebox.askyesnocancel("ask yes no cancel cancel","you are agree ")#title,message disply

def sumbit8():
    messagebox.askyesno("ask yes no","Yopu are good boy ")#title,message disply



#create a button 
sumbit_1 = tk.Button(root,text="Sumbit1",command=sumbit1).grid(row=4,column=2)
sumbit_2 = tk.Button(root,text="Sumbit2",command=sumbit2).grid(row=4,column=3)
sumbit_3 = tk.Button(root,text="Sumbit3",command=sumbit3).grid(row=5,column=2)
sumbit_4 = tk.Button(root,text="Sumbit4",command=sumbit4).grid(row=5,column=3)
sumbit_5 = tk.Button(root,text="Sumbit5",command=sumbit5).grid(row=6,column=2)
sumbit_6 = tk.Button(root,text="Sumbit6",command=sumbit6).grid(row=6,column=3)
sumbit_7 = tk.Button(root,text="Sumbit7",command=sumbit7).grid(row=7,column=2)
sumbit_8= tk.Button(root,text="Sumbit8",command=sumbit8).grid(row=7,column=3)

#run mainloop
root.mainloop()

#--------------bye Like and subcribe --------------------------