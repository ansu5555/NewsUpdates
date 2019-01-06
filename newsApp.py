import os
import json

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    api_key = os.environ.get('NEWSAPI_KEY')
    resp = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')
    resp_dict = json.loads(resp.text)
    articles = resp_dict['articles']
    return render_template('news.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
