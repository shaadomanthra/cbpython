from tkinter import *
from tkinter import ttk

# add functionality
def buttonPress():
    label.config(text="Hello")

root = Tk()
# add a text label
label = ttk.Label(root,text="Welcome")
label.grid(row=0,column=1)

# add a button
button = ttk.Button(root,text="Click Me",command = buttonPress)
button.grid(row=2,column=1)


