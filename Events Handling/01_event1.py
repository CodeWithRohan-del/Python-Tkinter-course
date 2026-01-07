import tkinter as tk

def on_left_click(event):
    label.config(text=f"Left Click at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Button-1 Event")
root.geometry("400x300")

label = tk.Label(root, text="Click anywhere in the window", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Button-1>", on_left_click)
root.mainloop()