from PIL import Image, ImageFilter

img = Image.open("./pokedex/pikachu.jpg")
print(img)

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png", 'png')

converted_image = img.convert('L')
converted_image.save("convert.png", "png")
# converted_image.show()

routing_image = converted_image.rotate(45)
routing_image.save("routed.png", "png")
# we can also resize the image with .resize((300,300)) to decrease the size of image

box1 = (100, 100, 400, 400)
cropped_image = img.crop(box1)
cropped_image.save("crop.png","png")
