from typing import Iterable
import random

from Project.adapters.repository import AbstractRepository
from Project.domain.model import Movie



def article_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
    }
    return movie_dict


def movie_to_dict(movie: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movie]
