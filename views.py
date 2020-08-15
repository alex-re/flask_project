from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, make_response, session
from flask_project import db
from flask_project.models import User, Writer, Books

@app.route("/")
def index():
    return "home page"
