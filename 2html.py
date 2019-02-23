'''we return html template here
we need to use render template method of the flask library
render template accesses HTML file stored somewhere in our python
application, in our python files and that displays that HTML of the requested url'''



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    # home.html must be stored in template folder

if __name__ == "__main__":
    app.run(debug = True)
