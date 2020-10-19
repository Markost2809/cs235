import csv

from Project.utilities.objects import Director, Movie, Genre, Actor


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
                movie.description = line["Description"]
                movie.runtime_minute = int(line["Runtime (Minutes)"])
                # Get Director
                director = Director(line["Director"])
                self.dataset_of_directors.append(director)
                movie.director = director
                # Get Genres
                for genres in line["Genre"].split(","):
                    genre = Genre(genres)
                    self.dataset_of_genres.append(genres)
                    movie.add_genre(genre)
                # Get Actors
                for actors in line["Actors"].split(","):
                    actor = Actor(actors)
                    self.dataset_of_actors.append(actor)
                    movie.add_actor(actor)
                # Get Description

                self.catalogue += [movie]

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
