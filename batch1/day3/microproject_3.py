from PIL import Image               # import the image package

im = Image.open('images/wallpaper.jpg')
print( im.size)

# resize image and save
im2 = im.resize((400,400))
im2.save('images/wallpaper_resized.jpg')
print(im2.size)

# resize image proportionately and save
im.thumbnail((400,400))
im.save('images/wallpaper_thumbnail.jpg')
print(im.size)
