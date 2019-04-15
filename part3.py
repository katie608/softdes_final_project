import random
from random import randint
from PIL import Image

#randomly generates x forground elements
"""
1. random selection from environment list
2. randomly places random selection onto screen
# """
ONE=["octo.jpg", "beachball.jpg", "eagle.png"] #BEACH
TWO=[] #FOREST
THREE=[] #MOUNTAIN
FOUR=[] #DESERT

num_to_select=randint(0,9)
list_of_random_images=random.sample(ONE,num_to_select)

# #-----------------------------------------

#overlay image onto final screen
"""
puts image onto other image (eg middleground (sand), and foreground (octopus))
"""
# #------the manual version------
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
sand=Image.open("sand.jpg")

for i in list_of_random_images:
    element=Image.open(i)
    sand.paste(element)

sand.show()
