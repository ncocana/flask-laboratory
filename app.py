from flask import Flask, render_template, request

# Turns this file into a Flask application.
app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Frisbee"
]

# In Python, this is called a "decorator".
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # "something?key=value" is called Query parameters/HTTP parameters.
        name = request.form.get("name", "World")
        if not name:
            return render_template("register-failure.html")
        return render_template("greet.html", name = name)

@app.route("/sports", methods=["GET", "POST"])
def sports():
    if request.method == "GET":
        return render_template("sports.html", sports=SPORTS)
    if request.method == "POST":
        name = request.form.get("name", "World")
        sport = request.form.get("sport", "No sport selected")
        if sport not in SPORTS or not name:
            return render_template("register-failure.html")
        REGISTRANTS[name] = sport
        return render_template("register-success.html", name = name, sport = sport)

@app.route("/sports/registrants")
def registrants():
    return render_template("registrants.html", registrants = REGISTRANTS)
