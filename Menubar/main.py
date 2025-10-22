
#-----------------Menubar in Tkinter python -----------------

#importing Tkinter 
import tkinter as tk 
 
#create a root object  
root =  tk.Tk()

#set window size
root.geometry("800x600")

#Cretae a welcome label 
label =  tk.Label(text="Welcome to Menubar Tutorial").pack()

#create a menubar

#Create a mainmenu 
main = tk.Menu(root)

#add menu option 
file_menu = tk.Menu(main,tearoff=0)

#create function to add cmmanf file menu function
def newtxt():
    print("I am Txt File")
def save():
    print("File saved..")
def open():
    print("opening file")

def open_folder():
    print("Opening Folder")
#add fuction in File menu
file_menu.add_command(label="New python file",command=newtxt)
#add sapretor
file_menu.add_separator()
file_menu.add_command(label="Open",command=open)
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Open Folder",command=open_folder)
file_menu.add_command(label='Exit',command=quit)#already 

#Add a main menu
main.add_cascade(menu=file_menu,label="File")

#adding other
main.add_cascade(menu=help,label="help")

#push the window
root.config(menu=main)



#run The mainloop
root.mainloop()

#------------------This is menubar