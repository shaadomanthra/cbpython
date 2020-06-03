from tkinter import *

class DetectionView:

    def load(self):
        window = Tk()
        frame = Frame(window,bg="yellow",padx=10,pady=10)
        frame.grid(row=0,column=0,padx=10,pady=10)

        l1 = Label(frame, text="welcome")
        l1.grid(row=0,column=0)

        window.mainloop()