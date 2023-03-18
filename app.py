from flask import Flask, render_template, request

# Turns this file into a Flask application.
app = Flask(__name__)

# In Python, this is called a "decorator".
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet')
def greet():
    name = request.args.get("name", "World")
    if name == "":
        name = "World"
    return render_template("greet.html", name = name)
