import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSON

from db.database import Base


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    url = Column(String(120))
    result_all = Column(JSON)
    result_no_stop_words = Column(JSON)
    meta = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

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


class Input(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True)
    meta = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, created_at=None, meta=None):
        if meta:
            self.meta = meta
        if created_at:
            self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, password, created_at=None):
        self.username = username
        self.password = password
        if created_at:
            self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
