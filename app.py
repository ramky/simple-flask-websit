from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

date = datetime.now()
year = date.strftime("%Y")


@app.route("/")
@app.route("/index")
def index():

    return render_template("index.html", active="home", year=year)


@app.route("/experience")
def experience():
    return render_template("experience.html", active="experience", year=year)


@app.route("/projects")
def projects():
    return render_template("projects.html", active="projects", year=year)


@app.route("/contact_me")
def contact_me():
    return render_template("contact_me.html", active="contact_me", year=year)
