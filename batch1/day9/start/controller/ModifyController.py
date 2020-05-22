## This controller is used to make changes to the Image

class Modify:
    width = 300
    height = 400

    def printSize(self,image):
        print(image.size)

    def imageResizeSave(self,image,width,height,path):
        im = image.resize((width,height))
        im.save(path)
        print("The image is successfully resized and saved")

    def imageRotate(self,image,degree,path):
        im = image.rotate(degree)
        im.save(path)
        print("The image is successfully rotated and saved")
