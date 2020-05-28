from tkinter import *
from controller.HelloController import Hello

class Layout:

    def __init__(self):
        self.root = Tk()
        h = Hello(self)

        self.b1 = Button(self.root, text=" hello basic ", command = h.hello_basic)
        self.b1.pack()

        self.b2 = Button(self.root, text="hello name", command=h.hello_name)
        self.b2.pack()

        self.b3 = Button(self.root, text="hello in french", command=h.hello_in_french)
        self.b3.pack()

        self.l1 = Label(self.root, text="Welcome")
        self.l1.pack()
