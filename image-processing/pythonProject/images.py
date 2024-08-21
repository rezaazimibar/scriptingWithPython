# from PIL import Image, ImageFilter
#
# img = Image.open("./pokedex/pikachu.jpg")
# astro = Image.open("./pokedex/astro.jpg")
#
# print(img)
#
# filtered_image = img.filter(ImageFilter.BLUR)
# filtered_image.save("blur.png", 'png')
#
# converted_image = img.convert('L')
# converted_image.save("convert.png", "png")
# # converted_image.show()
#
# routing_image = converted_image.rotate(45)
# routing_image.save("routed.png", "png")
# # we can also resize the image with .resize((300,300)) to decrease the size of image
#
# box1 = (100, 100, 400, 400)
# cropped_image = img.crop(box1)
# cropped_image.save("crop.png","png")
#
# astro_image = astro.size
# print(astro_image)
# new_astro = astro.resize((400, 400))
# new_astro.save("newAstro.png", "png")
#
# astro.thumbnail((400, 200))
# astro.save("newAstro1.png")
# print(astro.size)

# --------------------------------------------exercise--------------------------------------------

import os
import sys

from PIL import Image

my_folder = sys.argv[1]
your_folder = sys.argv[2]
folder_check = os.path.exists(your_folder)
if not folder_check:
    os.makedirs(your_folder)
try:
    my_folder_checker = os.listdir(my_folder)
    for i in my_folder_checker:
        img = Image.open(f'./pokedex/{i}')
        img.save(f"./{your_folder}/{os.path.splitext(i)[0]}.png", "png")
        # print(os.path.splitext(i),i[:-4])
except FileNotFoundError:
    print("the folder not exist")
