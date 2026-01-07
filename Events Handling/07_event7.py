import tkinter as tk

def on_leave(event):
    label.config(text="Mouse Left the Button!", fg="red")

def on_enter(event):
    label.config(text="Mouse on Button!", fg="green")

root = tk.Tk()
root.title("Leave Event")
root.geometry("400x300")

button = tk.Button(root, text="Hover Here", font=("Arial", 16), width=15, height=3)
button.pack(pady=30)

label = tk.Label(root, text="Move mouse over the button", font=("Arial", 12))
label.pack(pady=20)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
root.mainloop()