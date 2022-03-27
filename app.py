
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  date_joined = db.Column(db.Date, default=datetime.utcnow)
  
  def __repr__(self) -> str:
      return f'<User> {self.email}'
  
class Owner(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  address = db.Column(db.String(100))
  pets = db.relationship('Pet', backref='owner')
  
class Pet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  age = db.Column(db.Integer)
  owner_id = db.Column(db.Integer, db.ForeignKey('owner.id')) #parent table name in lower case eg: owner
  

