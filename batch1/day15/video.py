import cv2

# Load an color image in grayscale
cap = cv2.VideoCapture(0)
ret, img = cap.read()
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()