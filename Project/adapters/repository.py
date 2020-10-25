import abc
from typing import List
from datetime import date

from Project.domain.model import User, Movie, Review

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):

        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:

        raise NotImplementedError
    
    @abc.abstractmethod
    def add_movie(self, movie: Movie):

        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id: int) -> Movie:

        raise NotImplementedError
        
    @abc.abstractmethod
    def get_movies(self, id):

        raise NotImplementedError
    
    @abc.abstractmethod
    def get_number_of_movies(self):

        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:

        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:

        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, id_list):

        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):

        if review.user is None or review not in review.user:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Comment not correctly attached to an Article')

    @abc.abstractmethod
    def get_reviews(self):

        raise NotImplementedError
    

