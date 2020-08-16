from flask_project import app, db
from flask_wtf.csrf import CSRFProtect


# SQL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(55), nullable=False)  # unic=True
    password = db.Column(db.String(55), nullable=False)

    def __repr__(self):
        return self.name  # if i dont say User.[id, name, family, ...] return name with default


# class Writer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)


# class Books(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

#     writer_id = db.Column(db.Integer(), db.ForeignKey("writer.id"))
#     writer = db.relationship("Writer", backref=db.backref("books"))

# db.create_all()  # after each change

# ------------------------------------------------------------------------

# CSRF
csrf = CSRFProtect()
csrf.init_app(app)