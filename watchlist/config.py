import os

class Config:
    """General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blade:maziwa@localhost/watchlist'
    UPLOADED_PHOTOS_DEST = 'ap/static/photos'

    # email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("abdirahman.noor@student.moringaschool.com")
    MAIL_PASSWORD = os.environ.get("abdirahmanNOOR11")
class ProdConfig(Config):
    """Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blade:maziwa@localhost/watchlist_test'

class DevConfig(Config):
    """Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blade:maziwa@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
