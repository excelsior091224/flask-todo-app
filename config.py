import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///todo_db.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(32)