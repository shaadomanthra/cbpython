
class Modify:
    width=300
    height=300

    def imageResizeSave(self,image,w,h,path):
        size = image.size
        im = image.resize((w,h))
        im.save(path)
        print(f"Image successfully resized from({size[0]},{size[1]}) to({w},{h}) and saved")
