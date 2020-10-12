from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or password != user.password:
        flash("try again")
        return redirect(url_for("auth.login"))

    login_user(user, False, None, True, True)
    return "Login"


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    new_user = User(email=email, name=name, password=password)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user
    return redirect(url_for("main.landing"))


@auth.route("/fail")
def fail():
    return "hi"
