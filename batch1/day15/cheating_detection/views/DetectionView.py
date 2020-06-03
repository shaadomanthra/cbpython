from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import threading

class DetectionView:

    def load(self):

        window = Tk()
        frame = Frame(window)
        frame.grid(row=0,column=0)

        l1 = Label(frame,text="Webcamera")
        l1.grid(row=1,column=0)

        window.mainloop()
