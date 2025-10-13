
#------------------Entry Widget in Tkinter------------------#
# Use Entry widgets to input the data form column type digin

#Importining Tkinter 
import tkinter as tk

#create a Tk() class root object
root = tk.Tk()

#set the size of window 
root.geometry("700x500")

#create textvriable for input the data of Entry type of data string integer ,float 
name_var = tk.StringVar()
age_var = tk.IntVar()

#create a Entry
name_Entry = tk.Entry(root,textvariable=name_var).pack()
age_Entry = tk.Entry(root,textvariable=age_var).pack()

#Run the mainloop
root.mainloop()