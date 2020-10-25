from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import Project.adapters.repository as repo
import Project.utilities.utilities as utilities
import Project.movies.services as services


movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route("/movies", methods=['GET'])
def movies():
    movie_per_page = 4
    cursor = request.args.get('cursor')
    showcomments = request.args.get("view_comments_for")

    if cursor is None:
        cursor = 1
    else:
        cursor = int(cursor)

    first_movies_url = None
    last_movies_url = None
    next_movies_url = None
    prev_movies_url = None

    movies_dict = services.get_movies(repo.repo_instance)
    keys = [cursor,cursor + 1, cursor + 2, cursor + 3]
    movies = {k: movies_dict[k] for k in keys}

    if cursor > 1:
        prev_movies_url = url_for('movies_bp.movies', cursor=cursor - movie_per_page)
        first_movies_url = url_for('movies_bp.movies')

    if cursor + movie_per_page < len(movies_dict):
        next_movies_url = url_for('movies_bp.movies', cursor=cursor + movie_per_page)

        last_cursor = movie_per_page * int(len(movies_dict) / movie_per_page)
        if len(movies_dict) % movie_per_page == 0:
            last_cursor -= movie_per_page
        last_movies_url = url_for('movies_bp.movies', cursor=last_cursor)

    return render_template(
        "movies/movies.html",
        movies = movies,
        first_movies_url = first_movies_url,
        last_movies_url = last_movies_url,
        next_movies_url = next_movies_url,
        prev_movies_url = prev_movies_url,
        cursor = cursor
        
    )
    