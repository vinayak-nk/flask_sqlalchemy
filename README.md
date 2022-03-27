# flask_sqlalchemy

DB Operations
--------------

DB
----
Cmd
Set FLASK_APP=run.py
 
flask shell
from server.app import create_app
from server.models import db
from Config import DevConfig
 
db.create_all(app=create_app(DevConfig))
 
 
Cmd
-------
flask db init --> generate migrations folder
flask db migrate -m "added user table"
flask db upgrade
