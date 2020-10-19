from flask import Blueprint, render_template
from flask_login import login_required, current_user

from Project.utilities.movies import MovieFileCSVReader


main = Blueprint("main", __name__)


@main.route("/")
def landing():

    movies = MovieFileCSVReader("Project\Data\Data1000Movies.csv")
    movies.read_csv_file()
    movies_list = movies.get_catalogue()

    return render_template("main.html", movies=movies_list[:8])


@main.route("/<count>")
def pages(count):

    movies = MovieFileCSVReader("Project\Data\Data1000Movies.csv")
    movies.read_csv_file()
    movies_list = movies.get_catalogue()

    return render_template("main.html", movies=movies_list[count:count*8],count=count)