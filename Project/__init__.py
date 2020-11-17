from flask import Flask\

import os

import Project.adapters.repository as repo
from Project.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('Project', 'adapters', 'data')

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)


    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import Movies
        app.register_blueprint(Movies.movies_blueprint)

        from .authentication import auth
        app.register_blueprint(auth.authentication_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app
