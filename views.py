from flask_project import app, db
from flask_project.models import User, Writer, Books
from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, make_response, session

@app.route("/")
def index():
    return "home page"
