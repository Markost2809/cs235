from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def landing():
    return render_template("landing.html")


@main.route("/home")
@login_required
def profile():
    return render_template("main.html", name=current_user.name)