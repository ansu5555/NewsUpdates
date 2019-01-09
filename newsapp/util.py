import json
import os
from datetime import datetime

import requests
import click

from newsapp import app, db
from newsapp.models import News


def get_articles():
    api_key = os.environ.get('NEWSAPI_KEY')
    resp = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')
    resp_dict = json.loads(resp.text)
    return resp_dict.get('articles')


def create_news_object(news_article):
    return News(title=news_article.get('title'),
                publishedAt=datetime.strptime(news_article.get('publishedAt')[:-1], "%Y-%m-%dT%H:%M:%S"),
                description=news_article.get('description'),
                url=news_article.get('url'),
                urlToImage=news_article.get('urlToImage'))


def update_db():
    db_articles = [item.title for item in News.query.all()]
    articles = get_articles()
    objects = []
    for article in articles:
        obj = create_news_object(article)
        if obj.title not in db_articles:
            objects.append(obj)
    print('====>', len(objects))
    db.session.bulk_save_objects(objects)
    db.session.commit()


@app.cli.command('reload_db', help='Refresh the Database.')
def reload_db():
    articles = get_articles()
    objects = [create_news_object(article) for article in articles]
    db.drop_all()
    db.create_all()
    db.session.bulk_save_objects(objects)
    db.session.commit()
    click.echo(f'Database refresh completed {len(objects)} record(s) added')


@app.template_filter('longdate')
def longdate_filter(dt):
    return dt.strftime('%d-%b-%Y %I:%M %p')


@app.template_filter('shortdate')
def shortdate_filter(dt):
    return dt.strftime('%b %d')
