from flask import Flask
# import flask class from Flask framework

app = Flask(__name__)
# app is a Flask object variable (instantiation)
# __name__ is a special variable that gets the name of the python script for eg: __main__
# here python assign __name__ = __main__ when you execute this script

# When you import a script from another script importing script
# will get the name of imported script assigned to __name__

@app.route('/') #decorator '/' <- homepage ( you put url there)
def home():
    # this function defines what webpage will do

    # the output of this function is returned to the URL defined
    # in the decorator

    return "Website Content goes here!!"
    # return string
    # you can also return plain html pages

@app.route('/anotherfunction')
def anotherfunction():
    return "LOCALHOST:5000/anotherfunction"

if __name__ == "__main__":
    # if this script is imported from another script and that script
    # is ran, this section will not be executed since __name__ != __main__
    app.run(debug = True)
