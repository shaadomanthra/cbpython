from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import threading

class DetectionView:

    stop = False

    def load(self):

        window = Tk()
        window.title("Cheating Detection App")

        frame = Frame(window,padx=20,pady=20,bg="yellow")
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=1,column=0,columns=2)

        b1 = Button(frame,text="start",command= self.startCamera)
        b1.grid(row=2,column=0)

        b2 = Button(frame, text="stop",command=self.stopCamera)
        b2.grid(row=2, column=1)

        self.startCamera()

        window.mainloop()

    def startCamera(self):
        self.stop = False
        self.cap = cv2.VideoCapture(0)
        t = threading.Thread(target= self.webcam, args=())
        t.start()

    def webcam(self):
        try:
            ret, image_frame = self.cap.read()
            image_frame = cv2.resize(image_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            self.img = Image.fromarray(image_frame)

            colorimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
            grayimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            self.img = Image.fromarray(colorimage)
            img = ImageTk.PhotoImage(self.img)
            self.l1.configure(image=img)
            self.l1.image = img

            if self.stop == False:
                self.l1.after(10, self.webcam)
            else:
                self.l1.image = None


        except:
            print("Some error")

    def stopCamera(self):
        self.stop = True

 


