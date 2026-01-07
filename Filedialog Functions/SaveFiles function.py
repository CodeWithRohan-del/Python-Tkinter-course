
#------------SavefileFunction --------------------------

#Function :
# 1. asksave
# 2.asksaveas

#I am create code To clera this function usinf AI 

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("800x500")

#Global variable to track the current file path
current_file_path = None    

def openfilename():
    global current_file_path
    path_1 = filedialog.askopenfilename(
        title="Open Filename",
        filetypes=[("Python file", "*.py"), ("All files", "*.*")]
    )
    print(f"Selected File Path: {path_1}")
    
    if path_1:
        current_file_path = path_1
        # Update label
        result_label.config(text=f"Selected: {path_1}")
        
        # Read file content and display in Text widget
        try:
            with open(path_1, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)  # Clear previous content
                text_area.insert(tk.END, content)
        except Exception as e:
            result_label.config(text=f"Error reading file: {e}")    

def save_as_file():
    global current_file_path
    path = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[("Text file", "*.txt"), ("Python file", "*.py"), ("All files", "*.*")]
    )
    if path:
        current_file_path = path
        save_file()

def save_file():
    global current_file_path
    if current_file_path:
        try:
            content = text_area.get(1.0, tk.END)
            with open(current_file_path, 'w') as file:
                file.write(content)
            result_label.config(text=f"Saved: {current_file_path}")
        except Exception as e:
            result_label.config(text=f"Error saving file: {e}")
    else:
        save_as_file()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons
open_button = tk.Button(button_frame, text="Select File", command=openfilename)
open_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)

save_as_button = tk.Button(button_frame, text="Save As", command=save_as_file)
save_as_button.pack(side=tk.LEFT, padx=5)

# Label to display the selected path
result_label = tk.Label(root, text="No file selected", font=("Arial", 10))
result_label.pack(pady=5)

# Text Area to display file content
text_area = tk.Text(root, height=20, width=80)
text_area.pack(pady=10, padx=10)

#Run the mainloop
root.mainloop()
