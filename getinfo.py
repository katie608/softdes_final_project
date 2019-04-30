"""Python code using flask to get variables from a website
Katie Foster TODO:
Make gradient function
Implement heroku or somehow get this online
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

def generate_background(date):
    """Takes in date and generates a gradient background appropriate for the time
    """
    # use get_time function to extract hour and minute
    hour, minute = get_time(date)

    # dictionary that maps hours to gradients
    gradient_dict = {
    "00": "#001538,#000000", # night
    "01": "#001538,#000000", # night
    "02": "#001538,#000000", # night
    "03": "#001538,#000000", # night
    "04": "#001538,#000000", # night 4am
    "05": "#62492e,#252a3c,#15192c,#05050e", # 5am
    "06": "#8c4a5f,#827143,#526884,#18234f", # 6am
    "07": "#8c4a5f,#526884,#18234f", # 7am
    "08": "#8abbdb,#000547", # 8am
    "09": "#bdd8e3, #5782ae, #2a477e", # 9am
    "10": "#8ec2e5, #5782ae, #2a477e", # day 10am
    "11": "#8ec2e5, #5782ae, #2a477e", # day
    "12": "#8ec2e5, #5782ae, #2a477e", # day
    "13": "#8ec2e5, #5782ae, #2a477e", # day
    "14": "#8ec2e5, #5782ae, #2a477e", # day
    "15": "#8ec2e5, #5782ae, #2a477e", # day 3pm
    "16": "#9a8d8d,#728ca4, #5782ae, #2a477e", # 4pm
    "17": "#9a8d8d,#b1b09b,#8d9ea0, #586d89, #3e4c6c", # 5pm
    "18": "##8f4036,#f9bb73,#f1dab6,#aeb7c6,#6c82a7,#203865,#0a1335", # 6pm
    "19": "#8c3e22,#ad8760,#948975,#79818a,#4a5f82,#21325a,#090e28,#06091a", # 7pm
    "20": "#6d231d,#723d27,#62492e,#252a3c,#15192c,#05050e", # 8pm
    "21": "#62492e,#252a3c,#15192c,#05050e,#010414", # 9pm
    "22": "#001538,#000000", # night 10pm
    "23": "#001538,#000000", # night
    }

    # TODO: use dictionary to generate gradient image
    pass

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

# eventually going to be:
# generate_image(filename, scene, date, dims)
# return render_template('output.html', image=(filename? something?))
# where image is the background image.
# for now, this just creates an output page where the variables are rendered
    return render_template('output.html', scene=scene, date=date, dims=dims)





if __name__ == '__main__':
    # runs all doctests
    import doctest
    doctest.testmod()

    # runs local server with flask app
    # app.run()

    # runs on heroku
     app.run(host=HOST, port=PORT)
