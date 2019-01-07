import json
import os

import requests
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '781acf22041dc71f67c55eafe98584e5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/NewsSchema'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class News(db.Model):
    NewsID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.Text, nullable=False)
    PublishedOn = db.Column(db.DateTime, nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Url = db.Column(db.String(240), nullable=False)
    UrlToImage = db.Column(db.String(240), nullable=False)

    def __repr__(self):
        return f'{News.Title}'


@app.route("/")
def home():
    api_key = os.environ.get('NEWSAPI_KEY')
    resp = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')
    resp_dict = json.loads(resp.text)
    articles = resp_dict['articles']
    return render_template('news.html', articles=articles)
