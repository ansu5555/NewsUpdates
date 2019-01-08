from newsapp import db


class News(db.Model):
    newsID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    publishedAt = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(240), nullable=False)
    urlToImage = db.Column(db.String(240), nullable=False)

    def __repr__(self):
        return f'{self.title}'
