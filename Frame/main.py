
#--------------Create Frame in Tkinter ---------------

#importing Tkinter 
import tkinter as tk

#create a root object
root  = tk.Tk()

#set window size
root.geometry("800x600")

#set window background color
root.configure(bg="black")

#create Function 
def printhello():
    print("Hello")
def printThanks():
    print("Thanks ...")
def printsunmbit():
    print("Form sumbited")
def printharry():
    print("Hey Harry You are Good")
#Create a Frame 
frame = tk.Frame(root,bg="red",width=200,height=800)#pass frame width and height

#back four Button on frame 
button_1 = tk.Button(frame,text="print hello",command=printhello).pack(side="top")
button_2 = tk.Button(frame,text="print Thanks",command=printThanks).pack(side="top")
button_3 = tk.Button(frame,text="print sumbit",command=printsunmbit).pack(side="top")
button_4 = tk.Button(frame,text="print hey harry",command=printharry).pack(side="top")
frame.pack(side="left")
#RRun mainloop
root.mainloop()