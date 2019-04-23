import random
from random import randint
import math
from PIL import Image
#modified material in background.py

"""resize photos"""
image=Image.open('octo.png')
image.show()
image.thumbnail((400,400))
image.save("smallerocto.jpg")
image.show()
