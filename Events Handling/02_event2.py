
import tkinter as tk

def on_button_press(event):
    label.config(text="Button Pressed!", fg="red")

def on_button_release(event):
    label.config(text=f"Button Released at ({event.x}, {event.y})", fg="green")

root = tk.Tk()
root.title("ButtonRelease-1 Event")
root.geometry("400x300")

label = tk.Label(root, text="Press and release mouse button", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Button-1>", on_button_press)
root.bind("<ButtonRelease-1>", on_button_release)
root.mainloop()