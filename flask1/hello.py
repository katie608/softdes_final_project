"""Toolbox 2
Katie Foster
"""
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
    return render_template("input.html")

@app.route('/output', methods = ["GET","POST"])
def display_output():
    scene = request.form.get('scene')
    date = request.form.get('date')
    dims = request.form.get("dims")
    if scene == "":
        return render_template('error.html')
    return render_template('output.html', scene=scene, date=date, dims=dims)


@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)


# runs local server with our application
# if __name__ == '__main__' makes sure the server only runs if the script is
# executed directly from the Python interpreter
if __name__ == '__main__':
    app.run()
