from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
db = SQLAlchemy(app, session_options={
    'autocommit': False,
    'autoflush': False,
    'expire_on_commit': False
    })

from api import views
