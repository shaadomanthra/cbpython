from tkinter import *
from tkinter import ttk
from controller.HelloController import Hello

class ViewLayout:

    def __init__(self):
        self.master = Tk()
        self.createWidget()

    def createWidget(self):

        h = Hello(self)
        self.label = ttk.Label(self.master, text="Welcome")
        self.label.grid(row=1, column=1)

        self.b1 = ttk.Button(self.master, text="Hello", command= h.hello_basic)
        self.b1.grid(row=2, column=1)

        self.b2 = ttk.Button(self.master, text="Hello Name", command= h.hello_name)
        self.b2.grid(row=3, column=1)

        self.b3 = ttk.Button(self.master, text="Hello in French", command=h.hello_in_french)
        self.b3.grid(row=4, column=1)


