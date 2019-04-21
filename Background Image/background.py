import random
import math
from PIL import Image

def clear_background():
    """
    Generates a clear background image so that when overlayed on another page,
    the background of that page shows through.
    """
    clearbackground = Image.new("RGB", (255, 255))
    clearbackground.putalpha(0)
    return clearbackground

def background(s,x_size=255, y_size=255):
    """Generates background based on time of day and saves as an image file.
    Args:
        filename: string filename for image (should be .png)
        s: string that tells what time of day it is
        x_size, y_size: optional args to set image dimensions (default: 255)
    """
    background = Image.new("RGB", (x_size, y_size))
    pixels = background.load()
    for i in range(x_size):
        for j in range(y_size):
            x = i
            y = j
            if s == "sunrise":
                a = x*y
                b = y
                c = 0
            if s == "daytime":
                a = y
                b = y*x*x
                c = y*x*x
            if s == "evening":
                a = 0
                b = y
                c = x*y
            if s == "sunset":
                a = y
                b = 0
                c = y*y*y
            if s == "night":
                a = 0
                b = 0
                c = y
            pixels[i, j] = (
                a,
                b,
                c
            )
    return background

def middleground(s):
    """
    Based on the user decision, this creates an image file with the
    middleground that corresponds to that environment.
    Beach -> Sand image
    Forest -> Trees image
    Mountains -> Mountains image
    Desert -> Dry Sand image
    """
    if(s == "desert"):
        middleground = Image.open("sand.jpg")
        #middleground.resize((255,255))
        #middleground.crop((100,100,100,100))
        return middleground

def combine_back_middle(im1, im2):
    """
    This combines the the middleground and background images.
    """
    im1.paste(im2,(0,125))
    return im1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    im = background("sunrise")
    #im1 = clear_background()
    im2 = middleground("desert")
    #im2.show()
    background = combine_back_middle(im,im2)
    #background = combine_back_middle(im,im1)
    background.show()

    #background.show()
    #background.save("background.jpg")
