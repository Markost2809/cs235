import csv
import os
from datetime import date,datetime

from bisect import bisect, bisect_left, insort_left

from Project.adapters.repository import AbstractRepository

from Project.domain.model import User, Movie, Review,Director,Genre,Actor, make_review
class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = []
        self._movies_index = {}
        self._users = []
        self._review = []

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)
    

    def add_movie(self, movie: Movie):
        insort_left(self._movies,movie)
        self._movies_index[movie.id] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None

        try:
            movie = self._movies_index[id]
        except KeyError:
            pass
        return movie
    
    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movie) > 0:
            movie = self._movie[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movie) > 0:
            movie = self._movie[-1]
        return movie

    def get_movies(self):
        movies = self._movies_index
        return movies

    def get_movie_by_id(self, id_list):
        existing_ids = [id for id in id_list if id in self._movies_index]
        movies = [self._movies_index[id] for id in existing_ids]
        return movies

    def add_review(self, review: Review):

        if review.user is None:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None:
            raise RepositoryException('Comment not correctly attached to an Article')


    def get_reviews(self):
        pass



def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        for row in reader:

            row = [item.strip() for item in row]
            yield row

def load_movies(data_path: str, repo: MemoryRepository):
     for line in read_csv_file(os.path.join(data_path,"Data1000Movies.csv")):

            # Get Movies
        movie = Movie(line[1], int(line[6]),int(line[0]))
        movie.description = line[3]
        movie.runtime_minute = int(line[7])
        # Get Director
        director = Director(line[4])
        movie.director = director
        # Get Genres
        for genres in line[2].split(","):
            genre = Genre(genres)
            movie.add_genre(genre)
        # Get Actors
        for actors in line[5].split(","):
            actor = Actor(actors)
            movie.add_actor(actor)
        # Get Description
        repo.add_movie(movie)


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for line in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(line[1],line[2])
        repo.add_user(user)
        users[line[0]] = user
    return users


def load_reviews(data_path: str, repo: MemoryRepository, users):
    for data_row in read_csv_file(os.path.join(data_path, 'reviews.csv')):
        comment = make_review(
            review=data_row[3],
            user=users[data_row[1]],
            movie=repo.get_movie(int(data_row[2])),
            rating=data_row[4]
        )
        repo.add_review(comment)


def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_movies(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load reviews into the repository.
    load_reviews(data_path, repo, users)