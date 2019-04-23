import random
from random import randint
import math
from PIL import Image, ImageFile
#modified material in background.py

# """resize photos"""
# image=Image.open('octo.png')
# image.show()
# image.thumbnail((400,400))
# image.save("smallerocto.jpg")
# image.show()


""""save image as progressive image"""
ImageFile.MAXBLOCK = 2**20

img = Image.open("octo.png")
img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
img.show()
