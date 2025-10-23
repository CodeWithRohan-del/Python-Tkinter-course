
#------------------Add text Area On Tkinter window --------------\
#importing tkinter 
import tkinter as tk 

#Create a root object
root  =  tk.Tk()

#set window size
root.geometry("800x600")

#set window background color
root.configure(bg="black")

#create a text Area 
text_area = tk.Text(root,height=200,width=150,background="#7E7B7B")
text_area.pack(anchor="center")

#insert text
text_area.insert(tk.END,"write you text")
#Run the mainloop
root.mainloop()