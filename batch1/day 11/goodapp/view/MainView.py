from controller.GoodController import Good
from tkinter import *

class Main:

    def __init__(self):
        self.root = Tk()
        g = Good(self)

        self.button1 = Button(self.root, text="Click Good Basic",command = g.goodbasic)
        self.button1.pack()

        self.button2 = Button(self.root,text="Click Good Advanced", command = g.goodadvanced)
        self.button2.pack()

        self.label = Label(self.root,text="This is my label")
        self.label.pack()
