from flask import Blueprint, render_template

# this file saves all the routes that user can go within the website.  Not Auth related things.
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

