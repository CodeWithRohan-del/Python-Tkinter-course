
#----------------------Set the Geometry ,minsize and maxsize of window --------------
#Geometry - The window opening size is called Gepmetry

#minsize - The minmumsize of the window is called minsize

#maxsize - The maxmum size of the window is called maxsize 

#-----------------------Start Write code ---------------------

#--------------------Step 1 Importing Tkinter Module -----------------
import tkinter as tk

#----------------------step 2 Create a Tk() class Object   ------------------
root = tk.Tk()

#----------------step 3 set the size ------------------------
#set geometry
root.geometry("880x400")#pass the string WIDTH X HEIGHT

#set minsize 
root.minsize(200,300)#pass Integer WIDTH,HEIGHT

#set the maxsize
root.maxsize(1000,900)

#-------------------Last Step Run the main loop ---------------------
root.mainloop()

#---------------------------program is Ready -------------------
