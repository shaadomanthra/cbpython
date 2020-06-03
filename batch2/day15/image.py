from cv2 import cv2

img = cv2.imread('f1.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# pip install opencv-python
# pip uninstall opencv-python
