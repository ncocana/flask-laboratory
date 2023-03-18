from flask import Flask, render_template, request

# Turns this file into a Flask application.
app = Flask(__name__)

# In Python, this is called a "decorator".
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # "something?key=value" is called Query parameters/HTTP parameters.
        name = request.form.get("name", "World")
        if name == "":
            name = "World"
        return render_template("greet.html", name = name)
