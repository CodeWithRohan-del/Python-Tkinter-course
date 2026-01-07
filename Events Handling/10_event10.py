import tkinter as tk

def on_configure(event):
    label.config(text=f"Window Size: {event.width}x{event.height}")

root = tk.Tk()
root.title("Configure Event")
root.geometry("400x300")

label = tk.Label(root, text="Resize the window", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Configure>", on_configure)
root.mainloop()