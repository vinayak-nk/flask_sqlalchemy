from server.models import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  
  def __repr__(self) -> str:
      return f'User {self.name}-- {self.email}'