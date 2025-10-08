

#------------------Pack widgets and Label all important option -----------------

#--------------------pack all important options-------

# side = how to pack the label of the side ("left","right","top", "bottom")
# anchor = to pack the Label  specify position 
# > "n" - (top-center)
# > "e" - (top-right)
# > "w" - (top-left)
# > "s" - (bottom-center)
# > "nw" - (top-left)
# > "ne" - (top-right)
# >  "sw" - (bottom-left)
# > "se" - (bottom-right)

#  --------------Label important opitions ----------------------

# Brackground = The background is the blackground color of label text short form 'bg'
# foreground = The font color of label text short form 'fg='

# font = The font of the label text like fonts
# > Arial:("Arial",14,"bold")
# > Courier New:("courier new",16,"italic")
# > Helvetica:("Helvetica",14,"bold")

# borderwith = The borderwidth define the width of border short form 'bd='
# relif =  The boder decration to use this option like Broders
# > "flat"
# > "raised"
# > "sunken"
# > "groove"
# > "ridge"

#text = Text option the write the text of Label
# image =   image option to help the display image on the label
# file option to dis plat the file on label

# ------------------------------Start write code best explan -----------------------
# importing Tkinter Module 
import tkinter as tk

# create a Tk() class object 
root = tk.Tk()

#define the window size 
root.geometry("800x500")
#Set the window Title 
root.title("Explan the pack and Label options")

# create a label and strat to Apply option 
label = tk.Label(text="Welcome to Python Tkinter GUI BY Create a Code with Roihan \n And This is best course",fg="#3F0E0E",font=("Arial",14,"bold"),borderwidth=5,relief="sunken")
label.pack(side="top")

#Run the mainloop
root.mainloop()

# ------------------------------complete - -----------------------------------
