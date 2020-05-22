from PIL import Image
from controller.ModifyController import Modify

class ImageOptimizer:

    def run(self):
        image = Image.open('images/person.jpg');
        modify = Modify()
        modify.imageResizeSave(image,500,500,'images/teja_resized.jpg')

io = ImageOptimizer()
io.run()
