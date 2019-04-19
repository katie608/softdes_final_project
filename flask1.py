"""Attempt 1 at integration, and getting variables from the website
into the python
"""
import random
# imports flask class
from flask import Flask, render_template, request
import requests
# created an instance of the flask class
# first argument is the name of the application’s module or package
app = Flask(__name__)


# renders html hopefully
@app.route('/', methods = ["GET","POST"])
def index():
    return render_template("index.html")



# will render the output html with variables from first html
@app.route('/output', methods = ["GET","POST"])
def display_output():
    scene = request.form.get('scene')
    time = request.form.get('time')
    if scene == "":
        scene = random.randint(1,4)
    # elif time == "":
    #     return render_template('error.html')
    print("browser time: ", request.args.get("time"))
    time = request.args.get("time")
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return render_template('generated.html', scene=scene, time=time)


# runs local server with our application
# if __name__ == '__main__' makes sure the server only runs if the script is
# executed directly from the Python interpreter
if __name__ == '__main__':
    app.run()
