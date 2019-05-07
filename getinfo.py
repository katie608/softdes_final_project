"""Python code using flask to get variables from a website
Katie Foster TODO:
Make gradient function
Implement heroku or somehow get this online
figure out how to display the output of this program as a background image
"""


"""________________________Code for generating image_________________________"""

import random
from random import randint
import math
import numpy as np
from PIL import Image, ImageFile
from resizeimage import resizeimage

def divide_dims(dims):
    """takes in the variable dims (aka dimentions) from javascript/flask, and
    returns width and height

    >>> divide_dims("827,880")
    ('827', '880')

    >>> divide_dims("1679,892")
    ('1679', '892')

    """
    mid = dims.find(",")
    width = dims[0:mid]
    height = dims[mid+1:len(dims)]
    return width, height


def get_time(date):
    """takes in date from javascript/flask, and sets the variables hour and minute
    to their appropriate values

    >>> get_time("Tue Apr 23 2019 23:19:57 GMT-0400 (Eastern Daylight Time)")
    ('23', '19')

    >>> get_time("Wed Apr 24 2019 06:59:38 GMT+0300 (Asia Qatar Standard Time)")
    ('06', '59')
    """
    a = date.find(":")
    hour = date[a-2:a]
    minute = date[a+1:a+3]
    return hour, minute

def background(date):
    """Takes in date and picks a gradient background appropriate for the time
    """
    # use get_time function to extract hour and minute
    hour, minute = get_time(date)
    hour = 12#int(hour)
    if hour <= 4 or hour > 21:
        background = Image.open("static/Night.png")
        return background
    elif hour >= 10 and hour <= 15:
        background = Image.open("static/Day.png")
        return background
    else:
        background = Image.open("static/"+str(hour)+".png")
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
    if(s == "Beach"):
        middleground = Image.open("ocean.png")
        middleground = resizeimage.resize_cover(middleground,(2000,300))
        return middleground
    if(s == "Forest"):
        middleground = Image.open("forest.png")
        middleground = resizeimage.resize_cover(middleground,(2000,350))
        return middleground
    if(s == "Mountain"):
        middleground = Image.open("mountain.png")
        middleground = resizeimage.resize_cover(middleground,(2000,221))
        return middleground
    if(s == "Desert"):
        middleground = Image.open("sand.jpg")
        middleground = resizeimage.resize_cover(middleground,(2000,300))
        return middleground

def removewhitespace(object):
    """
    make white space transparent
    """
    img=Image.open("Foreground Objects/" + object)
    img=img.convert("RGBA")
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x,y] == (255, 255, 255, 255): #if see white
                pixdata[x,y] = (255, 255, 255, 0) #make transparent
    return img

def choose_list(s):
    """
    returns a list of filenames of images of objects that are present in each
    environment.
    """
    ONE=["octo.png", "tree.png", "sanddollar2.png", "plant.png", "hermitcrab2.png", "hermitcrab.png", "driftwood.png", "driftwood2.png", "driftwood1.png", "crab.png", "beachball.png", "bag.png"] #BEACH
    TWO=["yew.png", "wildflowers.png", "wildflowers2.png", "poppies.png", "mushroom3.png", "mushroom2.png", "fox1.png","wildflowers3.png"] #FOREST
    THREE=["flowershrub.png", "juniper.png", "planto.png", "mountaingoat.png", "large_thumbnail.png", "chipmunk1.png", "chipmunk2.png", "hummingbird.png", "shrubby.png","chipmunk3.png", "chipmunk4.png", "flyingsquirrel.png", "ferret.png", "bunny.png", "fernplant.png", "yew.png", "mountaingoat.png", "mrfern.png", "flowershrub.png"] #MOUNTAIN
    FOUR=["wildcat2.png", "wallace.png", "spikes.png", "optimisticlizard.png", "night.png", "lizardlizarding.png", "lizard2.png", "jackrabbit.png", "huhwhat-lizard.png", "grumpylizard.png", "georgy.png", "fred.png", "flowercacti.png", "fennec2.png", "cactus2.png", "cactus-transparent-prickly-pear-3.png", "cactflowery.png"] #"cact.jpg"#DESERT
    if s == "Beach":
        return ONE
    if s == "Forest":
        return TWO
    if s == "Mountain":
        return THREE
    if s == "Desert":
        return FOUR

def random_foreground_selection(rand_obj):
    """
    Takes in a list of random objects corresponding to a particular environment
    and returns a random selection of objects from that list stored in a new
    list.
    """
    num_to_select=randint(3,5)
    #the numbers depend on the list of pics on the environment
    list_of_random_images=random.sample(rand_obj,num_to_select)
    return(list_of_random_images)

def random_placement(background,middleground,modified_list,dims,scene):
    """
    Takes in an image and a list of random objects and returns a compressed
    image with the objects randomly placed on the image passed in.
    """
    w2, h2 = divide_dims(dims)
    print(w2,h2)
    width, height=middleground.size
    print(width,height)
    print(modified_list)
    for i in modified_list:
        element=removewhitespace(i)
        element.thumbnail((400,100))
        w,h = element.size
        if scene == "Forest":
            startwidth=randint(0,(width-w))
            startheight=randint(0,(height-h-30))
        else:
            startwidth=randint(0,(width-w))
            startheight=randint(0,(height-h))
        endwidth=startwidth+w
        endheight=startheight+h

        position=(startwidth,startheight,endwidth,endheight)
        middleground.paste(element,position,element)
    background.paste(middleground,(0,int(h2)-height))

    return background

def generate_image(filename, scene, date, dims):
    """Generate entire image and save as an image file.
    """
    back = background(date)
    middle = middleground(scene)
    fore = random_placement(back,middle,random_foreground_selection(choose_list(scene)),dims,scene)
    n = filename
    fore.save(n)
    return fore,n



"""________________________Code for making Flask work________________________"""

# code for heroku deployment
import os
import time

HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
PORT = int(os.environ.get('PORT', 5000))

# imports flask class
from flask import Flask, render_template, request
import requests
# created an instance of the flask class
# first argument is the name of the application’s module or package
app = Flask(__name__)

# tells which url should trigger our function. In this case, it is / because
# it is the homepage of the website.
@app.route('/', methods = ["GET","POST"])
def get_input():
    return render_template("index.html")

@app.route('/output', methods = ["GET","POST"])
def display_output():
    # gets variables from html form in html template
    scene = request.form.get('scene')
    date = request.form.get('date')
    dims = request.form.get("dims")
    pic = "static/Day/"+str(scene)+".png"
    image, name = generate_image(pic, scene, date, dims)



    time.sleep(0.5)
    return render_template('output.html', scene=scene, date=date, dims=dims, pic=pic)

if __name__ == '__main__':
    # runs all doctests
    import doctest
    doctest.testmod()

    # runs local server with flask app
    # app.run()

    # runs on heroku
    app.run(host=HOST, port=PORT)
