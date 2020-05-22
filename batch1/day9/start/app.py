from PIL import Image
from controller.ModifyController import Modify

class ImageOptimizer:

    def run(self):
        im = Image.open('images/wallpaper.jpg')
        m = Modify()
        m.printSize(im)
        m.imageResizeSave(im,500,500,'images/wallpaper_resized.jpg')

io = ImageOptimizer()
io.run()
