import random
from random import randint
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

def choose_list(s):
    """
    returns a list of random objects that are present in each environment
    environment.
    """
    ONE=["octo.png", "beachball.jpg", "eagle.png"] #BEACH
    TWO=[] #FOREST
    THREE=[] #MOUNTAIN
    FOUR=[] #DESERT
    if s == "beach":
        return ONE
    if s == "forest":
        return TWO
    if s == "mountain":
        return THREE
    if s == "desert":
        return FOUR

def random_foreground_selection(rand_obj):
    """
    Takes in a list of random objects corresponding to a particular environment
    and returns a random selection of objects from that list stored in a new
    list.
    """
    num_to_select=randint(1,2)
    #the numbers depend on the list of pics on the environment
    list_of_random_images=random.sample(rand_obj,num_to_select)
    return(list_of_random_images)

def random_placement(background,middleground,modified_list):

    """
    Takes in an image and a list of random objects and returns a compressed
    image with the objects randomly placed on the image passed in.
    """
    middleground.thumbnail((255,200))
    w2,h2 = middleground.size
    print(w2)
    print(h2)
    width, height=middleground.size
    height = 104
    print(width)
    print(height)
    print(modified_list)
    for i in modified_list:
        element=Image.open(i)
        w1,h1 = element.size
        print(w1)
        print(h1)
        element.thumbnail((20,20))
        w,h = element.size
        print(w)
        print(h)

        startwidth=randint(0,(width-w))
        startheight=randint(0,(height-h))
        endwidth=startwidth+w
        endheight=startheight+h

        position=(startwidth,startheight,endwidth,endheight)
        middleground.paste(element, position)
        background.paste(middleground,(0,151))

    return background

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    background = background("sunrise")
    #im1 = clear_background()
    middleground = middleground("desert")
    foreground = random_placement(background,middleground,random_foreground_selection(choose_list("beach")))
    foreground.show()
    foreground.save('foreground.jpg')
