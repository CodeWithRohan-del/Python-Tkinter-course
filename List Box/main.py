

#-------------------Add Listbox in Tkinter --------------------------

#importing Tkinter 
import tkinter as tk 

#create a root 
root =  tk.Tk()

#set window size 
root.geometry("1000x600")
#set window title 
root.title("List Box")

#create a list box 
list = tk.Listbox(root, width=20,height=30,bg="#5A5959")

#insert ite3m on list 
list.insert(tk.END,"Harry")
list.insert(tk.END,"Rohan")
list.insert(tk.END,"Shivansh")
list.insert(tk.END,"Shivam")
list.insert(tk.END,"Prabal")

list.pack(pady=10)
#Run the mainloop
root.mainloop()