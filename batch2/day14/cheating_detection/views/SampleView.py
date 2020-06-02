from tkinter import *
from tkinter import ttk

class SampleView:

    def __init__(self):
        # Create a TK window
        window = Tk()

        # Create a tab based container
        tab_control = ttk.Notebook(window)

        page1_frame = ttk.Frame(tab_control)
        tab_control.add(page1_frame, text="Page 1")

        page2_frame = ttk.Frame(tab_control)
        tab_control.add(page2_frame, text="Page 2")

        page3_frame = ttk.Frame(tab_control)
        tab_control.add(page3_frame, text="Page 3")

        tab_control.pack()


        print("This is construtor")
        self.page1(page1_frame)
        self.page2(page2_frame)
        self.page3(page3_frame)

        window.mainloop()


    def page1(self,page1_frame):
        l = Label(page1_frame,text="This is page 1")
        l.pack()

        print("This is page 1")

    def page2(self,page2_frame):
        l = Label(page2_frame, text="This is page 2")
        l.pack()
        print("This is page 2")

    def page3(self,page3_frame):
        l = Label(page3_frame, text="This is page 3")
        l.pack()
        print("This is page 3")

sample = SampleView()
