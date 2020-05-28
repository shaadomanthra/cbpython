from tkinter import *
import webbrowser

root = Tk()

def buttonPress():
    l.config(text="You have clicked it")
    webbrowser.open("https://packetprep.com")
    
b = Button(root, text="click me",command=buttonPress)
b.pack()

l = Label(root, text ="This is the welcome Text")
l.pack()


