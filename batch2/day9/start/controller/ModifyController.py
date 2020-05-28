## This controller is used to make changes to the Image

class Modify:

    def imageResizeSave(self,image,width,height,path):
        im = image.resize((width,height))
        im.save(path)
        print("The image is resized and saved")

    def imageRotateSave(self,image,degree,path):
        im = image.rotate(degree)
        im.save(path)
        print("The image is rotated")
