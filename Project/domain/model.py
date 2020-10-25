from datetime import date, datetime

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f'<Director {self.__director_full_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.director_full_name == self.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name : str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f'<Genre {self.__genre_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.genre_name == self.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Actor :
    actor_full_name =""
    def __init__(self, actor= None):
        if actor != "" and type(actor) == str:
            self.actor = actor 
            actor_full_name = actor
        else:
            self.actor = None
            actor_full_name = None
        self.colleagues = []
    def __eq__(self,other):
        return self.actor == other.actor
    def __lt__(self,other):
        return self.actor < other.actor
    def __repr__(self):
        return "<Actor " + str(self.actor) + ">"
    def __hash__(self):
        return hash(self.actor)
        
    def get_actor(self):
        return self.actor
    def add_actor_colleague(self,colleague):
        self.colleagues += [colleague]
        
    def check_if_this_actor_worked_with(self,colleague):
        for i in range(len(self.colleagues)):
            if self.colleagues[i] == colleague:
                return True
        return False

class Movie:

    def __set_title_internal(self, title: str):
        if title.strip() == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    def __set_release_year_internal(self, release_year: int):
        if release_year >= 1900 and type(release_year) is int:
            self.__release_year = release_year
        else:
            self.__release_year = None



    def __init__(self, title: str, release_year: int, id: int):

        self.__set_title_internal(title)
        self.__set_release_year_internal(release_year)

        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__id = id

    # essential attributes
    @property
    def id(self) -> int:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__set_title_internal(title)

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int):
        self.__set_release_year_internal(release_year)

    # additional attributes

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) is str:
            self.__description = description.strip()
        else:
            self.__description = None

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if isinstance(director, Director):
            self.__director = director
        else:
            self.__director = None

    @property
    def actors(self) -> list:
        return self.__actors

    def add_actor(self, actor: Actor):
        if not isinstance(actor, Actor) or actor in self.__actors:
            return

        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if not isinstance(actor, Actor):
            return

        try:
            self.__actors.remove(actor)
        except ValueError:
            # print(f"Movie.remove_actor: Could not find {actor} in list of actors.")
            pass

    @property
    def genres(self) -> list:
        return self.__genres

    def add_genre(self, genre: Genre):
        if not isinstance(genre, Genre) or genre in self.__genres:
            return

        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if not isinstance(genre, Genre):
            return

        try:
            self.__genres.remove(genre)
        except ValueError:
            # print(f"Movie.remove_genre: Could not find {genre} in list of genres.")
            pass

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, val: int):
        if val > 0:
            self.__runtime_minutes = val
        else:
            raise ValueError(f'Movie.runtime_minutes setter: Value out of range {val}')

    def __get_unique_string_rep(self):
        return f"{self.__title}, {self.__release_year}"

    def __repr__(self):
        return f'<Movie {self.__get_unique_string_rep()}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__get_unique_string_rep() == other.__get_unique_string_rep()

    def __lt__(self, other):
        if self.title == other.title:
            return self.release_year < other.release_year
        return self.title < other.title

    def __hash__(self):
        return hash(self.__get_unique_string_rep())


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text
        self.__rating = rating
        self.__timestamp = datetime.now()
        self.__user = ""

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    @property
    def user(self):
        return self.__user
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.movie == self.__movie and other.review_text == self.__review_text and other.rating == self.__rating and other.timestamp == self.__timestamp

    def __repr__(self):
        return f'<Review of movie {self.__movie}, rating = {self.__rating}, timestamp = {self.__timestamp}>'

class User:
    time_spent_watching_movies_minutes = 0

    def __init__(self, user, password):
        if user != "" and type(user) == str:
            self.username = user.strip().lower()
        else:
            self.username = None
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


def make_review(review:str,user:User,movie:Movie,rating:int):
    review = Review(Movie, review,rating)
    user.add_review(review)

    return review

