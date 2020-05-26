from tkinter import *
from tkinter import ttk


# add functionality
def buttonPress():
    label.config(text="Hello")

root = Tk()
# add a text label
label = ttk.Label(root,text="Welcome")
label.pack()


# add a button
button = ttk.Button(root,text="Click Me",command = buttonPress)
button.pack()

