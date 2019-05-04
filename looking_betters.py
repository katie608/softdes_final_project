import random
from random import randint
import math
import numpy as np
from PIL import Image, ImageFile
# modified material in background.py


# """"save image as progressive image"""
# ImageFile.MAXBLOCK = 2**20
#
# img = Image.open("octo.png")
# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
# img.show()


# """save files as progressive jpegs"""
# #this will be at the very end of the code to
# #save the final picture as progressive jpeg
# def final_save_image_settings():
#     img=Image.open("octo.png") #replace w/ final image from master Python code
#     img.save("softdes final project", format="JPEG", quality=95, progressive=True)
#     img.show()

# ---------------the new code to implement--------------



# """color overlay based on time of day, the final layer to put onto image generation
# current time modes:
#     dawn (pinkish)
#     morning and noon (no color overlay)
#     evening (sunset colors)
#     night (nighttime dark blue colors)
# """
# #note for when we merge code: we will need to get a folder for color overlay jpegs
# #to make sure we have everything neat
#
# def timecoloroverlay(): #then put daytime image onto the final image
#    if time == dawn: #question: is this based on the time recognition in the JavaScript code? Needs integration here
#         img = Image.open("dawnpink.png")
#         img.putalpha(10)
#         img.save()
#     elif time == noon or morning: #aka pure transparent overlay, or no overlay
#         return
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





"""sillhoutes of images based on time:
    dawn (sunrise, so light gray sillhoutes)
    noon and morning (no or transparent sillhouttes)
    evening (sunset, so dark gray sillhoutes)
    night (almost complete black/blue sillhoutte)
"""

modified_list=["octo.png"]
def removewhitespace():
    for i in modified_list:
        img=Image.open(i)
        img=img.convert("RGBA")
        pixdata = img.load()
        img.show()
        width, height = img.size
#the filters
        if time == dawn:
            img = img.point(lambda p: p * .25) #a light gray filter
        elif time == noon or morning:
            return
        elif time == evening:
            img = img.point(lambda p: p * .1) #dark grey filter
        elif time == night:
            img=img.point(lambda p: p*0) #black filter
#make white space transparent
        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x,y] == (255, 255, 255, 255): #if see white
                    pixdata[x,y] = (255, 255, 255, 0) #make transparent
