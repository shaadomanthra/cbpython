from PIL import Image
from controller.ModifyController import Modify

class ImageOptimizer:

    def run(self):
        im = Image.open('images/wallpaper.jpg')

        m = Modify()
        m.imageResizeSave(im)


io = ImageOptimizer()
io.run()
