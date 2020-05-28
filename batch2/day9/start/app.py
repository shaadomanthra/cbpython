from PIL import Image
from controller.ModifyController import Modify
from controller.ColorController import Color

class ImageOptimizer:

    def run(self):
        im = Image.open('images/wallpaper.jpg')

        m = Modify()
        # m.imageRotateSave(im,90,'images/wallpaper_rotated.jpg')

        c  = Color()
        c.blackwhite(im,'images/wallpaper_bw.jpg')

io = ImageOptimizer()
io.run()
