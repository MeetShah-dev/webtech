"""
    File: db_model
    Location: /model/db_model.py
    This module contain database tables required by various functions.

"""
from db.db_declarative_config import magazine_base
from sqlalchemy import Column, Integer, VARCHAR, DateTime


class Magazine(magazine_base):
    __tablename__ = 'magazine'
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(VARCHAR(255))
    date_created = Column(DateTime)
    date_released = Column(DateTime)
    magazine_flag = Column(VARCHAR(255))


class Job(magazine_base):
    __tablename__ = 'scheduled_jobs'
    __table_args__ = {"schema": "public"}
    magazine_id = Column(Integer)
    job_id = Column(VARCHAR(255), primary_key=True, autoincrement=False)
    status = Column(VARCHAR(255))
    magazine_title = Column(VARCHAR(255))
    updated_time = Column(DateTime)
    release_date = Column(DateTime)
