
#----------------------label and Widgets --------------------

#---------------------------Explan widgets ---------------
# There are three types on wegets 
#>pack() widget
#>grid() widget
#>place()widget\
#---pack()-pack widgets pack the Attribute on the window side and anchar
#--grid()-grid wiget pack the Atttribute on window colunm and row 
#--place() widget pack the Attribute on the window postion base

#-----------------Explan Label --------------------
#label is widbget to use the display image and text on window with formmating user not interact the label

#--------------------------START WRITE A CODE TO VERY EASSY AND EXPLAN ----------------
#-----------------------STEP 1 IMPORT THE TKINTER MODULE
import tkinter as tk 

#-------------------------STEP 2 CREATE TK() CLASS OBJECT--------------------------
root = tk.Tk()

#--------------------------STEP 3 CREATE A LABEL AND PACK ---------------------
label = tk.Label(text="Welcome to My GUI ")# you text=you want to Enter the text to Display the text
#This code go the tkinter and use label class 
#pack the label on window 
label.pack()

#---------------------STEP 4 RUN THE EVENT LOOP------------------
root.mainloop()

#---------------------------by end the video text topic to add the side title image on window -------------
