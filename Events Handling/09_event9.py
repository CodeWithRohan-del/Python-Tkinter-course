
import tkinter as tk

def on_ctrl_a(event):
    label.config(text="Ctrl+A pressed! (Select All)", fg="blue")
    text_widget.tag_add("sel", "1.0", "end")

root = tk.Tk()
root.title("Control-a Event")
root.geometry("400x300")

label = tk.Label(root, text="Press Ctrl+A to select all text", font=("Arial", 12))
label.pack(pady=10)

text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(pady=10)
text_widget.insert("1.0", "This is sample text.\nPress Ctrl+A to select all.")

root.bind("<Control-a>", on_ctrl_a)
root.mainloop()