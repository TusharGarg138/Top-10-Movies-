from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = "Your_API_key"
MOVIE_DB_SEARCH_URL = "themoviedb"
MOVIE_DB_INFO_URL = "themoviedb"
MOVIE_DB_IMAGE_URL = "URL"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seceret key'
Bootstrap5(app)

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
