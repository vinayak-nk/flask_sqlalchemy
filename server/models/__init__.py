from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def database_initialize(app):
    db.init_app(app)
    migrate = Migrate(app, db)

from server.models import users
