#part3.py randomly generates x forground elements and places them onto screen

import random
from random import randint
from PIL import Image

"""
random selection from environment requested (aka a list)
"""
ONE=["octo.jpg", "beachball.jpg", "eagle.png"] #BEACH
TWO=[] #FOREST
THREE=[] #MOUNTAIN
FOUR=[] #DESERT

def random_foreground_selection():
    num_to_select=randint(1,2) #the numbers depend on the list of pics on the environment
    list_of_random_images=random.sample(ONE,num_to_select)
    return(list_of_random_images)

# random_foreground_selection()
"""
randomly places random selection onto screen
"""
#------the manual version------
# sand=Image.open("sand.jpg")
# beachball=Image.open("beachball.jpg")
# octo=Image.open("octo.jpg")
#
# a=(100,100, 650,650)
# m=(10,10,910,530)
#
# sand.paste(beachball, a) #puts beachball on sand, with specifi coords
# sand.paste(octo,m)
# #sand.show()

# -----the automatic version------
middleground=Image.open("sand.jpg")
width, height=middleground.size

def random_placement(middleground):

    for i in random_foreground_selection():
        element=Image.open(i)
        w,h = element.size

        startwidth=randint(0,width)
        startheight=randint(0,height)
        endwidth=startwidth+w
        endheight=startheight+h

        position=(startwidth,startheight,endwidth,endheight)
        middleground.paste(element, position)

    middleground.show()

random_placement(middleground)
