import os
import json
from datetime import datetime

import requests

from newsapp import db
from newsapp.models import News


def update_db():
    api_key = os.environ.get('NEWSAPI_KEY')
    resp = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')
    resp_dict = json.loads(resp.text)
    articles = resp_dict['articles']
    print('json count ===>', len(articles))
    objects = []
    for article in articles:
        obj = News(title=article['title'],
                   publishedAt=datetime.strptime(article['publishedAt'][:-1], "%Y-%m-%dT%H:%M:%S"),
                   description=article['description'],
                   url=article['url'],
                   urlToImage=article['urlToImage'])
        objects.append(obj)
    print('objects count ===>', len(objects))
    db.drop_all()
    db.create_all()
    db.session.bulk_save_objects(objects)
    db.session.commit()
