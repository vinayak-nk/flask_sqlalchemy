import os
from flask import Flask

def create_app(config):
  app = Flask(__name__)
  os.environ['FLASK_ENV'] = config.FLASK_ENV
  app.config.from_object(config)

  @app.route('/')
  def hello():
    return 'hello world'

  return app