from flask_project import app, db
from flask_wtf.csrf import CSRFProtect


# SQL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(55), nullable=False)  # unic=True
    password = db.Column(db.String(75), nullable=False)
    name = db.Column(db.String(55), nullable=False)

    def __repr__(self):
        return self.name  # if i dont say User.[id, name, family, ...] return name with default


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("contents"))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)



db.create_all()  # after each change

# ------------------------------------------------------------------------

# CSRF
csrf = CSRFProtect()
csrf.init_app(app)