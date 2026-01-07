
import tkinter as tk

def on_double_click(event):
    label.config(text=f"Double-Clicked at ({event.x}, {event.y})!", bg="yellow")

root = tk.Tk()
root.title("Double-Button-1 Event")
root.geometry("400x300")

label = tk.Label(root, text="Double-click anywhere", font=("Arial", 14), bg="white")
label.pack(pady=20, fill=tk.BOTH, expand=True)

root.bind("<Double-Button-1>", on_double_click)
root.mainloop()