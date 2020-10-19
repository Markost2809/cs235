import csv
from datetime import datetime


class MovieFileCSVReader():
    def __init__(self, filename):
        self.filename = filename
        self.dataset_of_movies = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []
        self.dataset_of_actors = []
        self.catalogue = []

    def read_csv_file(self):
        with open(self.filename, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                # Get Movies
                movie = Movie(line["Title"], int(line["Year"]))
                # Get Director
                if movie != None:
                    movie.director(Director(line["Director"]))
                    # Get Genres
                    for genres in line["Genre"].split(","):
                        movie.add_genre(Genre(genres))
                    # Get Actors
                    for actors in line["Actors"].split(","):
                        movie.add_actor(Actor(actors))
                    # Get Description
                    movie.description = line("Description")

    def get_movies(self):
        return self.dataset_of_movies

    def get_directors(self):
        return self.dataset_of_directors

    def get_genres(self):
        return self.dataset_of_genres

    def get_actors(self):
        return self.dataset_of_actors

    def get_catalogue(self):
        return self.catalogue


class Director:
    def __init__(self, director="None"):
        self.director = director

    def __eq__(self, other):
        return self.director == other.director

    def __lt__(self, other):
        return self.director < other.director

    def __repr__(self):
        if self.director != "":
            return "<Director " + self.director + ">"
        else:
            return "<Director None>"

    def __hash__(self):
        return hash(self.director)


class Genre:
    def __init__(self, genre="None"):
        self.genre = genre

    def __eq__(self, other):
        return self.genre == other.genre

    def __lt__(self, other):
        return self.genre < other.genre

    def __repr__(self):
        if self.genre != "":
            return "<Genre " + self.genre + ">"
        else:
            return "<Genre None>"

    def __hash__(self):
        return hash(self.genre)


class Actor:
    def __init__(self, actor="None"):
        self.actor = actor
        self.colleagues = []

    def __eq__(self, other):
        return self.actor == other.actor

    def __lt__(self, other):
        return self.actor < other.actor

    def __repr__(self):
        if self.actor != "" and type(self.actor) == str:
            return "<Actor " + self.actor + ">"
        else:
            return "<Actor None>"

    def __hash__(self):
        return hash(self.actor)

    def add_actor_colleague(self, colleague):
        self.colleagues += [colleague]

    def check_if_this_actor_worked_with(self, colleague):
        for i in range(len(self.colleagues)):
            if self.colleagues[i] == colleague:
                return True
        return False


class Movie:
    description = ""
    actors = []
    genres = []
    title = ""

    def __init__(self, movie=None, year=None):
        if movie != "":
            self.movie = movie
        else:
            self.movie = None
        if year >= 1900:
            self.year = year
        else:
            self.year = None
        self.title = self.movie.strip()
        self._director = None
        self._runtime_minutes = None

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if type(value) == Director and self._director == None:
            self._director = value

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, value):
        if value <= 0:
            raise ValueError
        else:
            self._runtime_minutes = value

    def __eq__(self, other):
        return self.movie == other.movie and self.year == other.year

    def __lt__(self, other):
        return self.movie < other.movie

    def __repr__(self):
        return "<Movie " + self.movie + ", " + str(self.year) + ">"

    def __hash__(self):
        return hash((self.movie, self.year))

    def add_actor(self, actor):
        if actor not in self.actors and type(actor) == Actor:
            self.actors += [actor]

    def remove_actor(self, actor):
        if actor in self.actors and len(self.actors) > 0:
            self.actors.pop(self.actors.index(actor))

    def add_genre(self, genre):
        if genre not in self.genres and type(genre) == Genre:
            self.genres += [genre]

    def remove_genre(self, genre):
        if genre in self.genres and len(self.genres) > 0:
            self.genres.pop(self.genres.index(genre))


class Review:
    def __init__(self, movie, review, rating):
        self.movie = movie
        self.review_text = review
        if rating >= 1 and rating <= 10:
            self.rating = rating
        else:
            self.rating = None

    def __repr__(self):
        return "<" + str(self.movie) + ", " + str(self.review_text) + ", " + str(self.rating) + ">"

    def __eq__(self, other):
        return self.review_text == other.review_text and self.review_text.datetime == other.review_text.datetime


class User:
    time_spent_watching_movies_minutes = 0

    def __init__(self, user, password):
        if user != "" and type(user) == str:
            self.user_name = user.strip().lower()
        else:
            self.user_name = None
        if password != "" and type(password) == str:
            self.password = password
        else:
            self.password = None
        self._watched_movies = []
        self._reviews = []

    @property
    def watched_movies(self):
        return self._watched_movies

    @watched_movies.setter
    def watched_movies(self, value):
        if type(value) == Movie:
            self._watched_movies += [value]

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if type(value) == Review:
            self._reviews += [value]

    def __repr__(self):
        return "<User " + str(self.user_name) + ">"

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if type(movie) == Movie:
            self.watched_movies += [movie]
            if movie.runtime_minutes and movie.runtime_minutes > 0:
                self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) == Review:
            self.reviews += [review]
