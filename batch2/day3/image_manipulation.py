from PIL import Image               # import the image package

im = Image.open('teja.jpg')       # load image
print(im.format, im.size)           # print the format size
im = im.convert("L").rotate(180)     # turn to grayscale and rotate
im.show()                           # open in windows
im.save('updated.jpg', quality=95)  # save it to computer
