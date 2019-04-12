import random
from random import randint
from PIL import Image

#randomly generates x forground elements to overlay
"""
1. random selection from environment list
2. randomly places random selection onto screen
"""
# ONE=['KRAKEN','CRAB','BEACHBALL','PALM TREE','SEASHELL','SEAGULL','UMBRELLA','GIANT SQUID', "SUNTAN LOTION", 'MONKEY'] #BEACH
# TWO=[] #FOREST
# THREE=[] #MOUNTAIN
# FOUR=[] #DESERT
#
# num_to_select=randint(0,9)
# list_of_random_images=random.sample(ONE,num_to_select)
#
# print(list_of_random_images)
# -----------------------------------------



background = Image.open(r"/home/yjiang/softdes_final_project/eagle.png")
overlay = Image.open(r"/home/yjiang/softdes_final_project/octo.jpg")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("new.png","PNG")
