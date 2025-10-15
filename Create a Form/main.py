#----------Create a Form in Tkinter user data input -------

#step1 - Importing Tkinter 
import tkinter as tk

#step2 - Create a Tk() class root objects
root = tk.Tk()

#step3 - set the window size
root.geometry("700x400")

#step4 - Create a welcome text use Label
welcome  = tk.Label(text="Welcome to GUI Form in Tkinter ",font=("Arial",16,"bold"))
welcome.grid(row=0,column=2)

#step5 - Create a Label for show text - name ,age ,phone address and Emial
name = tk.Label(text="Name")
age  = tk.Label(text="Age")
phone = tk.Label(text="Phone")
address= tk.Label(text="Address")
email= tk.Label(text="Email")

#step6 - pack the label using grid
name.grid(row=1,column=1)
age.grid(row=2,column=1)
phone.grid(row=3,column=1)
address.grid(row=4,column=1)
email.grid(row=5,column=1)

#step7 - Create a textvriable for Entry
name_var = tk.StringVar()
age_var = tk.StringVar()
phone_var = tk.StringVar()
add_var = tk.StringVar()
email_var = tk.StringVar()
check_var = tk.IntVar()

#step8 - Create a Entry
name_entry = tk.Entry(root,textvariable=name_var)
age_entry = tk.Entry(root,textvariable=age_var)
phone_entry = tk.Entry(root,textvariable=phone_var)
add_entry = tk.Entry(root,textvariable=add_var)
email_entry = tk.Entry(root,textvariable=email_var)

#step9 - pack the Entry
name_entry.grid(row=1,column=2)
age_entry.grid(row=2,column=2)
phone_entry.grid(row=3,column=2)
add_entry.grid(row=4,column=2)
email_entry.grid(row=5,column=2)

#step10 - create checkbuttons for text you are 18 Year older
label =  tk.Label(text="You are 18 Year older")
label.grid(row=6,column=2)
check_buttons = tk.Checkbutton(root,textvariable=check_var)
check_buttons.grid(row=6,column=2)

#create a function For sumbit form button after subiting form to the data write on text file 
def sumbit():
    with open("records.text","a") as f:
        data = f"Name:{name_var.get()}\nAge:{age_var.get()}\n Phone:{phone_var.get()}\n Address:{add_var.get()}\n emial:{email_var.get()}\n\n"
        f.write("This is user data")
        f.write(data)
    print("Form is sumbited data is stored..")

#create a button 
buttons  =  tk.Button(root,text="Sumbit",command=sumbit)
buttons.grid(row=7,column=2)

#step11 - Run the mainloop()
root.mainloop()

#--------form is Ready -----------------------------
