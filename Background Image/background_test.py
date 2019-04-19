import random
import math
from PIL import Image

def time_of_day(t):
    """Converts time of day to a string that categorizes the time
    as sunrise, daytime, evening, sunset, or night
    """

def generate_art(filename,s,x_size=255, y_size=255):
    """Generates background based on time of day and saves as an image file.
    Args:
        filename: string filename for image (should be .png)
        s: string that tells what time of day it is
        x_size, y_size: optional args to set image dimensions (default: 255)
    """

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    im3 = Image.new("RGB",(x_size, y_size))
    im2 = im.putalpha(0)
    pixels = im3.load()
    for i in range(x_size):
        for j in range(y_size):
            x = i
            y = j
            if s == "sunrise":
                a = x*y
                b = y
                c = 0
            # if s == "daytime":
            #     a = y
            #     b = y*x*x
            #     c = y*x*x
            # if s == "evening":
            #     a = 0
            #     b = y
            #     c = x*y
            # if s == "sunset":
            #     a = y
            #     b = 0
            #     c = y*y*y
            # if s == "night":
            #     a = 0
            #     b = 0
            #     c = y
            pixels[i, j] = (
                # color_map(evaluate_random_function(red_function, x, y)),
                # #color_map(0),
                # color_map(evaluate_random_function(green_function, x, y)),
                # color_map(evaluate_random_function(blue_function, x, y))
                a,
                b,
                c
            )
    
    im4 = Image.blend(im2,im3,0.5)
    im4.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    generate_art("background.png","sunrise")
