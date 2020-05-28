from tkinter import *

class MyApp:

    def __init__(self):
        self.root = Tk()
        self.b1 = Button(self.root,text="Click Me",command=self.buttonPress)
        self.b1.pack()

        self.l1 = Label(self.root, text="This is welcome")
        self.l1.pack()

        

    def buttonPress(self):
        self.l1.config(text="You have Clicked it")


app = MyApp()




