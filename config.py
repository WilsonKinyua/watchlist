import os


class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://developer:developerwilson@localhost/watchlist'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {'development': DevConfig, 'production': ProdConfig}
