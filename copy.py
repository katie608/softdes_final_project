import random
from random import randint
import math
import numpy as np
from PIL import Image, ImageFile

"""
Saves image as progressive image.
Implement this at the very end of image generation
"""
img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)


"""
color overlay based on time of day
this is the final layer to put onto image generation
current time modes:
    dawn (pinkish)
    morning and noon (no color overlay)
    evening (sunset colors)
    night (nighttime dark blue colors)
"""
def timecoloroverlay():
   if time == dawn:
        img = Image.open("dawnpink.png") #<--- will need to download a pinky png for this to work
        img.putalpha(10)
        img.save()
    elif time == noon or morning: #aka pure transparent overlay, or no overlay
        return
    elif time == evening:
        img=Image.open("eveningyaleblue.png") #<--- will need to download a blue png for this to work
        img.putalpha(10)
        img.save()
    elif time == night:
        img=Image.open("darkblue.png") #<--- will need to download a blue png for this to work
        img.putalpha(15)
        img.save()
    else:
        return


"""
removes white space around picture (if there is any)

the "else" statement below will create a black sillhoutte
not sure how or where we would put that into the master code
"""
def removewhitespace():
    for i in modified_list:
        img=Image.open(i)
        img=img.convert("RGBA")
        pixdata = img.load()
        width, height = img.size

        for y in xrange(height):
            for x in xrange(width):
                if pixdata[x,y] == (255, 255, 255, 255): #if it sees white
                    pixdata[x,y] = (255, 255, 255, 0) #make transparent


        #the following lines of code makes a black sillhoutte of the image for nighttime
                else:
                     pixel = img.getpixel((x,y))
             pixdata[x,y] = (pixel[0] * 0,pixel[1] * 0 ,pixel[2]* 0)  #make a for loop here to do filter colors
