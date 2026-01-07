

# <center>Events in Python Tkinter<center>

## Bind() event Methods
- ### `<Button-1>`	Left mouse button pressed (1, 2, 3 for left, middle, right)	`x, y (coordinates)`
- ### `<ButtonRelease-1>`	Left mouse button released	`x, y (coordinates)`
- ### `<Double-Button-1>`	Left mouse button double-clicked	
- ### `<B1-Motion>`	Mouse moved while left button held down	`x, y (coordinates)`
- ### `<Motion>`	Mouse moved within widget (no button held)	`x, y (coordinates)`
- ### `<Enter>`	Mouse pointer enters the widget area	
- ### `<Leave>`	Mouse pointer leaves the widget area	
- ### `<Key> / <KeyPress>`	Any key is pressed	`char, keysym, keycode`
- ### `<Return>`	The Enter key is pressed	`keysym`
- ### `<Control-a>`	Ctrl + 'a' is pressed	`keysym`
- ### `<FocusIn>`	Widget gains keyboard focus	
- ### `<Configure>`	Widget changes size or location	`width, height`
# Practical Application Examples
## 1. `<Button-1>` Method
**Description:** The `<Button-1>` event is triggered when the **Left Mouse Button** is pressed on the widget. It is the most fundamental interaction for detecting clicks.
```Python
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
```
## 2. `<ButtonRelease-1>` Method
**Description:** The `<ButtonRelease-1>` event fires when the **Left Mouse Button is released**. This is often used to complete a click action, ensuring the user finished the press.
```Python
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
```
## 3. `<Double-Button-1>` Method
**Description:** The `<Double-Button-1>` event detects a **Double-Click** with the left mouse button. It is used for quick interactions like opening a file or expanding an item.
```Python
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
```
## 4. `<B1-Motion>` Method
**Description:** The `<B1-Motion>` event is triggered when the mouse is **moved** while the **Left Button is held down** (dragging). This is essential for drawing applications or drag-and-drop features.
```Python
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
```
## 5. `<Motion>` Method
**Description:** The `<Motion>` event fires whenever the mouse pointer **moves** over the widget, regardless of whether any button is pressed. It tracks mouse movement in real-time.
```Python
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
```
## 6. `<Enter>` Method
**Description:** The `<Enter>` event is triggered when the mouse pointer **enters** the widget's area. It is commonly used to trigger hover effects, like changing a button's color.
```Python
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
```
## 7. `<Leave>` Method
**Description:** The `<Leave>` event fires when the mouse pointer **leaves** the widget's area. It is used to revert changes made during the `<Enter>` event (e.g., removing a highlight).
```Python
import tkinter as tk

def on_leave(event):
    label.config(text="Mouse Left the Button!", fg="red")

def on_enter(event):
    label.config(text="Mouse on Button!", fg="green")

root = tk.Tk()
root.title("Leave Event")
root.geometry("400x300")

button = tk.Button(root, text="Hover Here", font=("Arial", 16), width=15, height=3)
button.pack(pady=30)

label = tk.Label(root, text="Move mouse over the button", font=("Arial", 12))
label.pack(pady=20)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
root.mainloop()
```
## 8. `<Key>` / `<KeyPress>` Method
**Description:** The `<Key>` or `<KeyPress>` event detects any **keyboard key press**. The event object contains details like the character typed (`char`) and the specific key code.
```Python
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
```
## 9. `<Control-a>` Method
**Description:** This event represents a specific **Keyboard Shortcut** binding (Control + A). You can bind specific key combinations to trigger functions, like "Select All" in a text editor.
```Python
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
```
## 10. `<Configure>` Method
**Description:** The `<Configure>` event is a system event that triggers when the widget is **resized**, moved, or its properties change. It is useful for handling dynamic layout adjustments.
```Python
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
```