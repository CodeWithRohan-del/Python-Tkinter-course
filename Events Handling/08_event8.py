import tkinter as tk

def on_key_press(event):
    label.config(text=f"Key Pressed: '{event.char}' (keycode: {event.keycode})")

root = tk.Tk()
root.title("Key/KeyPress Event")
root.geometry("400x300")

label = tk.Label(root, text="Press any key", font=("Arial", 14))
label.pack(pady=20)

root.bind("<Key>", on_key_press)
root.mainloop()