from datetime import datetime
from flask import render_template

from newsapp import app
from newsapp.models import News


@app.route("/")
def home():
    timenow = datetime.now()
    articles = News.query.order_by(News.publishedAt).all()
    return render_template('news.html', articles=articles, timenow=timenow)
