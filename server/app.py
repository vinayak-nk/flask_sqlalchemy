import os
from flask import Flask

from server.models import database_initialize

def create_app(config):
  app = Flask(__name__)
  # os.environ['FLASK_ENV'] = config.FLASK_ENV
  app.config.from_object(config)
  database_initialize(app)

  @app.route('/')
  def hello():
    return 'hello world'

  return app