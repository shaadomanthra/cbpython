## This controller is used to change color of image

class Color:

    def grey(self,image,path):
        im = image.convert("L")
        im.save(path)
        print("The image is converted into greyscale")

    def blackwhite(self,image,path):
        im = image.convert("1")
        im.save(path)
        print("The image is converted into black and white")
