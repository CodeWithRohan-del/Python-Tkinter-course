import tkinter as tk

def on_drag(event):
    label.config(text=f"Dragging at ({event.x}, {event.y})")
    canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill="blue")

root = tk.Tk()
root.title("B1-Motion Event (Drawing)")
root.geometry("500x400")

label = tk.Label(root, text="Click and drag to draw", font=("Arial", 12))
label.pack(pady=5)

canvas = tk.Canvas(root, bg="white", width=480, height=350)
canvas.pack(pady=10)

canvas.bind("<B1-Motion>", on_drag)
root.mainloop()