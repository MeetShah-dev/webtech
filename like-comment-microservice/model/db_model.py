"""
    File: db_model
    Location: /model/db_model.py
    This module contain database tables required by various functions.
"""

from db.db_declarative_config import magazine_base
from sqlalchemy import Column, Integer, VARCHAR, DateTime, Text, Boolean

class Comment(magazine_base):
    __tablename__ = 'comment'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    timestamp = Column(DateTime)
    blog_id = Column(Integer)
    user_id = Column(Integer)

class Like(magazine_base):
    __tablename__ = 'like'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    blog_id = Column(Integer)
    user_id = Column(Integer)
    value = Column(VARCHAR(255))

class Blog(magazine_base):
    __tablename__ = 'blog'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(VARCHAR(255))
    content = Column(Text)
    is_approved = Column(Boolean)
    is_draft = Column(Boolean)
    is_rejected = Column(Boolean)
    rejection_number = Column(Integer)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    reader_ids = Column(VARCHAR(255))
    keywords = Column(VARCHAR(255))
    likes = Column(Integer)
    comments = Column(Integer)
    readers = Column(Integer)
    magazine_id = Column(Integer)
    user_id = Column(Integer)
    is_ready = Column(Boolean)
