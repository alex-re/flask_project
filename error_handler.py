from flask import render_template
from flask_wtf.csrf import CSRFError


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return e.description, 400



@app.errorhandler(404)
def error404handler(error):
    return "Hi ! \n error is : \n \n \n" + str(error), 404
