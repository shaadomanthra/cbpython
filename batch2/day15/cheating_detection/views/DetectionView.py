from tkinter import *
from cv2 import cv2
from PIL import Image           # pip install pillow
from PIL import ImageTk
import threading

class DetectionView:

    def load(self):
        window = Tk()
        window.title("Cheating Detection App")
        frame = Frame(window,bg="yellow",padx=10,pady=10)
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=0,column=0)
        self.startCamera()
        window.mainloop()

    def startCamera(self):

        self.cap = cv2.VideoCapture(0)
        t = threading.Thread(target=self.webcam,args=())
        t.start()


    def webcam(self):

        ret, frame = self.cap.read()
        colorimg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(colorimg)
        imgtk = ImageTk.PhotoImage(img)

        self.l1.config(image=imgtk)
        self.l1.image = imgtk

        self.l1.after(10,self.webcam)

