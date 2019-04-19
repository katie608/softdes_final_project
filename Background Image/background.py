import random
import math
from PIL import Image

def clear_background():
    """
    Generates a clear background image so that when overlayed on another page,
    the background of that page shows through.
    """
    background = Image.new("RGB", (255, 255))
    background.putalpha(0)
    return background

def background(s,x_size=255, y_size=255):
    """Generates background based on time of day and saves as an image file.
    Args:
        filename: string filename for image (should be .png)
        s: string that tells what time of day it is
        x_size, y_size: optional args to set image dimensions (default: 255)
    """
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
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
                # color_map(evaluate_random_function(red_function, x, y)),
                # #color_map(0),
                # color_map(evaluate_random_function(green_function, x, y)),
                # color_map(evaluate_random_function(blue_function, x, y))
                a,
                b,
                c
            )
    return im

def middleground(s):
    """
    Based on the user decision, this creates an image file with the
    middleground that corresponds to that environment.
    Beach -> Sand image
    Forest -> Trees image
    Mountains -> Mountains image
    Desert -> Dry Sand image
    """
    if(s == "beach"):
        middleground = Image.open("sand.jpg")
        middleground.resize((255,255))
        #middleground.crop((0,100,100,0))
        return middleground

def combine_back_middle(im1, im2):
    """
    This combines the the middleground and foreground images.
    """
    im = Image.blend(im1,im2,0.5)
    return im


# def generate_art(filename,s,x_size=255, y_size=255):
#     """Generates background based on time of day and saves as an image file.
#     Args:
#         filename: string filename for image (should be .png)
#         s: string that tells what time of day it is
#         x_size, y_size: optional args to set image dimensions (default: 255)
#     """
#     # Create image and loop over all pixels
#     im = Image.new("RGB", (x_size, y_size))
#     im.putalpha(0)
#     im3 = Image.new("RGB",(x_size, y_size)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    im = background("sunrise")
    #im1 = clear_background()
    im2 = middleground("beach")
    background = combine_back_middle(im,im2)
    #background = combine_back_middle(im,im1)
    background.show()

    #background.show()
    #background.save("background.jpg")
