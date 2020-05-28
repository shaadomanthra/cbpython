from tkinter import *
from controller.HelloController import Hello

class Layout:

    def __init__(self):
        self.root = Tk()
        h = Hello(self)

        self.b1 = Button(self.root, text="click me", command = h.hello_basic)
        self.b1.pack()

        self.l1 = Label(self.root, text="Welcome")
        self.l1.pack()
