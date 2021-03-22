"""An example of a single page Flask application"""

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)

# app routes
# @ is python decorrator notation


@app.route('/')
def hello_world():
    return 'This is the "/" route'


@app.route('/an_endpoint')
def an_endpoint():
    return 'This is the "/an_endpoint" route'


# Create Astronouts table
SQL_equivalent = """
  CREATE TABLE Astronauts (
   id INTEGER PRIMARY KEY,
   username VARCHAR(80) NOT NULL,
   email VARCHAR(120) NOT NULL,
);
"""


class Astronauts(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(80), nullable=False)
    email = DB.Column(DB.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
