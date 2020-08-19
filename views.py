from flask_project import app, db
from flask_project.models import User  # , Writer, Books, csrf
from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, make_response, session
from hashlib import sha256


@app.route("/", methods=["POST", "GET"])
def index():
    return "home page"




@app.route("/signup")
def signup():
    return render_template("signup.html")



@app.route("/dashbord", methods=["POST", "GET"])
def dashboard():
        if "email" in request.form and "password" in request.form:
            email = request.form["email"]
            password = sha256(request.form["password"].encode()).hexdigest()
            if request.form["comming_from"] == "signup":
                try:
                    user = User(email=email, password=password)
                    db.session.add(user)
                    db.session.commit()
                    return render_template("dashbord.html", email=email, password=password)
                except:
                    return "error in create user"
            else:
                return render_template("dashbord.html", email=email, password=password)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create_content")
def create_content():
    return render_template("create_content.html")
    
