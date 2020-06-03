# import the computer vision library
# import cv2
from cv2 import cv2
# enable the webcamera
cap = cv2.VideoCapture(0)

# do a continuous image capture
while True:
    ret, frame = cap.read()  # This will take one image from webcam
    # push the imaage on the window
    cv2.imshow('Video', frame)

    # do this as long as someone presses the escape key for 1 sec
    c = cv2.waitKey(1)
    if c == 27:
        break

#  release the webcamera & destroy the window
cap.release()
cv2.destroyAllWindows()
