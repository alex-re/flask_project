from flask_project import app, db
from flask_project.models import User  # , Writer, Books, csrf
from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, make_response, session


@app.route("/", methods=["POST", "GET"])
def index():
    return "home page"


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")



@app.route("/dashbord", methods=["POST", "GET"])
def dashboard():
    email = request.form["email"]
    password = request.form["password"]        
    try:
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template("dashbord.html", email=email, password=password)
    except:
        return "permission denied", 404