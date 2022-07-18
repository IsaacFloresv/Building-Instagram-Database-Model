import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    fullname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    profile_picture = Column(String(250), default='#example')
    posts = Column(String(250), nullable=False) 
    followers = Column(String(250), nullable=False)
    following = Column(String(250), nullable=False)
    date_at = Column(DateTime, default=datetime.datetime.now())

    def to_dict(self):
        return{}

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Posts', backref='Posts')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users, primaryjoin=user_id == Users.id)

    def to_dict(self):
        return{}

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Posts', backref='Posts')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users, primaryjoin=user_id == Users.id)
    comment = Column(String(250))

    def to_dict(self):
        return{}

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author_id = Column(String(250), nullable=False)
    author = relationship(Users, primaryjoin=author_id == Users.id)
    image = Column(String(250), nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    likes_id = Column(String(250), nullable=False)
    likes = relationship(Likes, primaryjoin=likes_id == Likes.id)
    comments_id = Column(String(250), nullable=False)
    comments = relationship(Comments, primaryjoin=comments_id == Comments.id)
    date_at = Column(DateTime, default=datetime.datetime.now())

    def to_dict(self):
        return{}









## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e