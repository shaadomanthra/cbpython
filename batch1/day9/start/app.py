from PIL import Image
from controller.ModifyController import Modify
from controller.ColorController import Color

class ImageOptimizer:

    def run(self):
        im = Image.open('images/wallpaper.jpg')

        # Modify
        m = Modify()
        m.printSize(im)
        m.imageResizeSave(im,500,500,'images/wallpaper_resized.jpg')
        m.imageRotate(im,90,'images/wallpaper_r90.jpg')

        # Color
        c = Color()
        c.grey(im,'images/wallpaper_grey.jpg')
        c.blackwhite(im,'images/wallpaper_bw.jpg')

io = ImageOptimizer()
io.run()
