import os
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# get the directory of file being edited

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #  prevent sql alchemy from setting up a session to 
    # track inserts, updates, and deletes for models
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # to log queries generated

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')



class ProdConfig(Config):
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')
    DEBUG = False


config_dict = {
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}

config_chosen = config_dict[os.environ.get('CONFIG_CHOSEN')]