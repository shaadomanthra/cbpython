from tkinter import *
from tkinter import messagebox
from cv2 import cv2
from PIL import Image           # pip install pillow
from PIL import ImageTk
import threading

class DetectionView:
    stop = False

    def load(self):

        window = Tk()
        window.title("Cheating Detection App")
        frame = Frame(window,bg="#63cdda",padx=20,pady=20)
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=0,column=0,columns=3)

        b1 = Button(frame, text="start",command= self.startCamera,pady=15)
        b1.grid(row=1,column=0,sticky="nesw",pady=10)

        b2 = Button(frame, text="stop", command=self.stopCamera,pady=15)
        b2.grid(row=1, column=1,sticky="nesw",pady=10)

        b3 = Button(frame, text="capture", command=self.captureImage, pady=15)
        b3.grid(row=1, column=2, sticky="nesw", pady=10)

        self.l2 = Label(frame,text="Camera started",font=("Courier", 30),pady=20)
        self.l2.grid(row=2,column=0,columns=3,sticky="nesw")

        self.startCamera()
        window.mainloop()

    def startCamera(self):

        self.stop = False

        self.cascade = cv2.CascadeClassifier('lib/nose.xml')

        # create an instance for video capture via webcam
        self.cap = cv2.VideoCapture(0)

        #  start the process by threading - to run processes parallely
        t = threading.Thread(target=self.webcam,args=())

        t.start()

    def webcam(self):

        # capture each frame (image)
        ret, frame = self.cap.read()
        frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        # change the color to RBG
        colorimg = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        r = self.cascade.detectMultiScale(grayimg,1.7,11)

        if len(r) != 0:
            for (x,y,w,h) in r:
                cv2.rectangle(colorimg,(x,y),(x+w,y+h),(0,255,0),3)
                self.l2.config(text="Mask is not used properly")
        else:
            self.l2.config(text="User has covered his face")

        # converting the image to tkinter compatible image
        self.img = Image.fromarray(colorimg)
        imgtk = ImageTk.PhotoImage(self.img)

        # push the image into the tkinter label
        self.l1.config(image=imgtk)
        self.l1.image = imgtk

        # loop this process for every 10ms
        if self.stop == False:
            self.l1.after(10,self.webcam)
        else:
            self.l1.image = None

    def stopCamera(self):
        self.stop = True

    def captureImage(self):
        image = self.img
        try:
            image.save('images/1.jpg')
            messagebox.showinfo('Alert','Image is saved')
        except:
            messagebox.showinfo('Alert', 'Some error in saving image')










