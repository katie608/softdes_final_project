""" Code to display a different image based on the user's scene selection
on heroku. Will only display one of 4 images with same day background.
This is just for demonstration purposes and does not actually generate an image
"""

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
    pic = "static/"+str(scene)+"2.png"

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
