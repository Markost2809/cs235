from typing import List, Iterable

from Project.adapters.repository import AbstractRepository
from Project.domain.model import make_review, Movie, Review


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_comment(article_id: int, comment_text: str, username: str, repo: AbstractRepository):
    # Check that the article exists.
    article = repo.get_article(article_id)
    if article is None:
        raise NonExistentMovieException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    comment = make_comment(comment_text, user, article)

    # Update the repository.
    repo.add_comment(comment)


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_id)

    if movie is None:
        raise NonExistentMovieException

    return movie_to_dict(article)


def get_first_Movie(repo: AbstractRepository):

    movie = repo.get_first_Movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):

    movie = repo.get_last_movie()
    return movie_to_dict(movie)

def get_movies(repo: AbstractRepository):
    movies = repo.get_movies()
    return movies

def get_number_of_movies(repo: AbstractRepository):
    number = repo.get_number_of_movies()
    return number

def get_comments_for_article(article_id, repo: AbstractRepository):
    article = repo.get_article(article_id)

    if article is None:
        raise NonExistentArticleException

    return comments_to_dict(article.comments)


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'id': movie.id,
        'title': movie.title,
        'description': movie.description,
        'comments': reviews_to_dict(article.comments),
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def review_to_dict(review: Review):
    review_dict = {
        'movie': review.movie,
        'comment_text': review.review,
        'timestamp': review.timestamp
    }
    return review_dict


def reviews_to_dict(reviews: Iterable[Review]):
    return [comment_to_dict(review) for review in reviews]


"""def tag_to_dict(tag: Tag):
    tag_dict = {
        'name': tag.tag_name,
        'tagged_articles': [article.id for article in tag.tagged_articles]
    }
    return tag_dict


def tags_to_dict(tags: Iterable[Tag]):
    return [tag_to_dict(tag) for tag in tags]
"""

# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_article(dict):
    article = Article(dict.id, dict.date, dict.title, dict.first_para, dict.hyperlink)
    # Note there's no comments or tags.
    return article
