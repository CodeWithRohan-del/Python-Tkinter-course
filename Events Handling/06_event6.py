import tkinter as tk

def on_enter(event):
    event.widget.config(bg="lightblue", text="Mouse Entered!")

def on_leave(event):
    event.widget.config(bg="white", text="Hover over me")

root = tk.Tk()
root.title("Enter Event")
root.geometry("400x300")

label = tk.Label(root, text="Hover over me", font=("Arial", 14), bg="white", width=20, height=5)
label.pack(pady=50)

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)
root.mainloop()