import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '781acf22041dc71f67c55eafe98584e5'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/NewsSchema'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from newsapp import routes, util
