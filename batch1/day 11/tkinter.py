from tkinter import *

class Window:

    def __init__(self):

        self.root = Tk()

        self.b1 = Button(self.root, text = "click me",command = self.hellobasic)
        self.b1.pack()

        self.l1 = Label(self.root, text = "Welcome")
        self.l1.pack()

    def hellobasic(self):
        
        self.l1.config(text = "You have pressed click me button")


        
w = Window()
    




