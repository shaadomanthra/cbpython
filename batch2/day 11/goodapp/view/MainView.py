from controller.GoodController import Good
from tkinter import *

class Main:

    def __init__(self):
        print("The Main Controller is invoked")
        g= Good(self)
        self.master = Tk()
        self.b1 = Button(self.master, text="Basic Click",command = g.good_basic)
        self.b1.pack()

        self.b2 = Button(self.master, text="Advanced Click",command = g.good_advanced)
        self.b2.pack()

        self.label = Label(self.master, text = "Welcome to this good appliccation")
        self.label.pack()




