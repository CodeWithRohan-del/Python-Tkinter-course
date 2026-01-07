
import tkinter as tk

def on_motion(event):
    label.config(text=f"Mouse Position: ({event.x}, {event.y})")

root = tk.Tk()
root.title("Motion Event")
root.geometry("400x300")

label = tk.Label(root, text="Move your mouse", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Motion>", on_motion)
root.mainloop()