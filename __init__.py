from flask import jsonify, Flask, render_template, request, redirect, url_for, abort, make_response, session
import os
from flask_wtf.csrf import CSRFProtect, CSRFError
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# create db  -------------------------------------------------------
file_dir = os.path.dirname("/home/ali/flask/")
goal_route = os.path.join(file_dir, "app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary_key=True
    name = db.Column(db.String(50), nullable=False)  # 50 char maximum  (unique=True)

    def __repr__(self):
        return self.name  # if i dont say User.[id, name, family, ...] return name with default


class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    writer_id = db.Column(db.Integer(), db.ForeignKey("writer.id"))
    writer = db.relationship("Writer", backref=db.backref("books"))



db.create_all()  # after each change

#--------------------------------------------------------------------


app.permanent_session_lifetime = timedelta(days=1)


# make directory named "uploaded_files"
path = os.path.join("uploaded_files")
os.makedirs(path, exist_ok="True")


# app.secret_key = b"\x03I\xcd\xb5\xd1\xaa\x1c\x89B\x1e\xc0\xb30ZW\t\xff\xcam\n@\x95\xb9\xd7"
app.secret_key = os.urandom(24)
csrf = CSRFProtect()
csrf.init_app(app)

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    # return render_template('csrf_error.html', reason=e.description), 400
    return e.description, 400
