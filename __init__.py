from flask import Flask
# import os
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app = Flask(__name__)


# SQL
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "/home/ali/flask/flask_project/app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# SESSION
app.permanent_session_lifetime = timedelta(days=1)


# CSRF
app.secret_key = os.urandom(24)

from flask_project import models, views