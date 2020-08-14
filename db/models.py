import datetime
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSON

from myapp import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)
    meta = db.Column(JSON, nullable=True)
    created_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, url, result_all, result_no_stop_words, created_at=None,
                 meta=None):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words
        if meta:
            self.meta = meta
        if created_at:
            self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
