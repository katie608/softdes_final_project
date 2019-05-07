""" Code to display a different image based on the user's scene selection
on heroku. Will only display one of 4 images with same day background.
This is just for demonstration purposes and does not actually generate an image
"""


def get_hour(date):
    """takes in date from javascript/flask, and sets the variable hour to
    what the hour is

    >>> get_hour("Tue Apr 23 2019 23:19:57 GMT-0400 (Eastern Daylight Time)")
    '23'

    >>> get_hour("Wed Apr 24 2019 06:59:38 GMT+0300 (Asia Qatar Standard Time)")
    '06'
    """
    a = date.find(":")
    hour = date[a-2:a]

    return hour


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

    hour = get_hour(date)
    hour = int(hour)
    if hour <= 4 or hour > 21:
        pic = "static/"+"Night/"+str(scene)+".png"
    elif hour >= 10 and hour <= 15:
        pic = "static/"+"Day/"+str(scene)+".png"
    else:
        pic = "static/"+str(hour)+"/"+str(scene)+".png"


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
