from ctypes import cast
from distutils.debug import DEBUG
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
  SECRET_KEY = config('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)
  
class DevConfig(Config):
  SQLALCHEMY_ECHO = True
  DEBUG=True
  SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'dev.db'))
  # FLASK_ENV=config('FLASK_ENV_DEV') 

class ProdConfig(Config):
  SQLALCHEMY_ECHO = True
  DEBUG=True
  FLASK_ENV=config('FLASK_ENV_PROD')
  SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'prod.db'))


class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI= 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.db'))
  SQLALCHEMY_ECHO=False
  TESTING=True
  # FLASK_ENV=config('FLASK_ENV_DEV')

# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')

# load_dotenv(dotenv_path)