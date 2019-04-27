import random
from random import randint
import math
import numpy as np
from PIL import Image, ImageFile
#modified material in background.py

# """resize photos"""
# image=Image.open('octo.png')
# image.show()
# image.thumbnail((400,400))
# image.save("smallerocto.jpg")
# image.show()

# """"save image as progressive image"""
# ImageFile.MAXBLOCK = 2**20
#
# img = Image.open("octo.png")
# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
# img.show()

#-----------the new code to implement--------------

# """color overlay based on time of day, the final layer to put onto image generation
# current time modes:
#     dawn
#     morning
#     noon
#     evening
#     night
# """
# def timecoloroverlay(): #then put daytime image onto the final image
#     if time == dawn: #question: is this based on the time recognition in the JavaScript code? Needs integration here
#         img = Image.open("dawnpink.png")
#         img.putalpha(10)
#         img.save()
#     elif time == morning:
#         img=Image.open("lightblue.png")
#         img.putalpha(10)
#         img.save()
#     elif time ==noon: #a pure transparent overlay
#         img=Image.open("nocolor.png")
#         img.putalpha(0)
#         img.save()
#     elif time == evening:
#         img=Image.open("eveningyaleblue.png")
#         img.putalpha(10)
#         img.save()
#     elif time == night:
#         img=Image.open("darkblue.png")
#         img.putalpha(15)
#         img.save()
#     else:
#         return


# """make all white pixels around foreground objects transparent"""
# img = Image.open('octo.png')
# img = img.convert("RGBA")
# pixdata = img.load()
#
# width, height = img.size
# for y in xrange(height):
#     for x in xrange(width):
#         if pixdata[x, y] == (255, 255, 255, 255):
#             pixdata[x, y] = (255, 255, 255, 0)
# img.show()
# img.save("img2.png", "PNG")




"""sillhoutes of images""" ###STOPPED HERE
im=Image.open("octo.png")
im=im.convert("RGBA")


#---------version one
pixdata = img.load()

# Clean the background noise, if color != white, then set to black.

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (0, 0, 0, 255)

img.show()


#---------version two
# data = np.array(im)   # "data" is a height x width x 4 numpy array
# red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
#
# # Replace white with red... (leaves alpha values alone...)
# white_areas = (red == 255) & (blue == 255) & (green == 255)
# data[..., :-1][white_areas.T] = (255, 0, 0) # Transpose back needed
#
# im2 = Image.fromarray(data)
# im2.show()
