"""
============================================================
SHARED DATABASE MODELS — models.py
============================================================
This file defines the database schema using SQLAlchemy ORM.

WHO USES THIS FILE:
  - The Data Engineer imports it to know what columns to fill in
    when saving posts to the database.
  - The Backend Developer imports it to query posts out of the
    database for the API.

This file is SHARED — both the pipeline and the backend point
at the same models.py and the same lobsters.db SQLite file.

============================================================
STUDENT TASK (Data Engineer leads this, whole team reviews it)
============================================================
Define ONE table: `posts`

Columns required:
  id            INTEGER, primary key, auto-increment
  post_id       STRING, unique, NOT NULL
  title         STRING, NOT NULL
  author        STRING, NOT NULL
  score         INTEGER, NOT NULL
  num_comments  INTEGER, NOT NULL
  url           STRING, NOT NULL
  permalink     STRING, NOT NULL
  created_utc   FLOAT, NOT NULL
  fetched_at    DATETIME, NOT NULL
============================================================
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)

    post_id = Column(String, unique=True, nullable=False)

    title = Column(String, nullable=False)

    author = Column(String, nullable=False)

    score = Column(Integer, nullable=False)

    num_comments = Column(Integer, nullable=False)

    url = Column(String, nullable=False)

    permalink = Column(String, nullable=False)

    created_utc = Column(Float, nullable=False)

    fetched_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Post id={self.id} title={self.title[:30]!r} score={self.score}>"

    def to_dict(self) -> dict:
        """
        Converts this Post object into a dictionary.
        Useful later for the backend API.
        """
        return {
            "id": self.id,
            "post_id": self.post_id,
            "title": self.title,
            "author": self.author,
            "score": self.score,
            "num_comments": self.num_comments,
            "url": self.url,
            "permalink": self.permalink,
            "created_utc": self.created_utc,
            "fetched_at": self.fetched_at.isoformat() if self.fetched_at else None,
        }