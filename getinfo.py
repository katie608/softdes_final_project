"""Python code using flask to get variables from a website
Katie Foster TODO:
figure out how to display the output of this program as a background image
"""


"""________________________Code for generating image_________________________"""

import random
import math
from PIL import Image

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

def pick_gradient(date):
    """Takes in date and picks a gradient background appropriate for the time
    """
    # use get_time function to extract hour and minute
    hour, minute = get_time(date)

    if int(hour) <= 4 or int(hour) > 21:
        pic = "Night.png"
    elif int(hour) >= 10 and int(hour) <= 15:
        pic = "Day.png"
    else:
        pic = str(hour)+".png"

    return pic

def generate_middleground(scene, width, height):
    """Generates a middleground of the image (on top of the gradient background?
    separately and then put them together?)
    """
    # TODO: put code here
    pass

def generate_foreground(scene, width, height):
    """Generates a foreground of the image (on top of the gradient background
    and middleground? separately and then put them together?)
    """
    # TODO: put code here
    pass


def generate_image(filename, scene, date, dims):
    """Generate entire image and save as an image file.
    """
    generate_background(date)
    width, height = divide_dims(dims)
    generate_middleground(scene, width, height)
    generate_foreground(scene, width, height)
    # TODO: If we are putting them all together, add some code here for that
    im.save(filename)
    pass







"""________________________Code for making Flask work________________________"""

# code for heroku deployment
import os

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
    pic = pick_gradient(date)

# eventually going to be:
# generate_image(filename, scene, date, dims)
# return render_template('output.html', image=(filename? something?))
# where image is the background image.
# for now, this just creates an output page where the variables are rendered
    return render_template('output.html', scene=scene, date=date, dims=dims, pic=pic)





if __name__ == '__main__':
    # runs all doctests
    import doctest
    doctest.testmod()

    # runs local server with flask app
    # app.run()

    # runs on heroku
    app.run(host=HOST, port=PORT)
