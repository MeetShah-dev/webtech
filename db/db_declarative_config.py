from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from logs.logging_handler import success_logger, error_logger

DB_NAME = "<DB_NAME>"
DB_USERNAME = "<DB_USERNAME>"
DB_PASSWORD = "<DB_PASSWORD>"
DB_HOST = "<DB_HOST>"
DB_PORT = "<DB_PORT>"
SQLALCHEMY_ECHO = True
DB_CONNECTION_POOL_SIZE = <DB_CONNECTION_POOL_SIZE>
DB_CONNECTION_MAX_OVERFLOW = <DB_CONNECTION_MAX_OVERFLOW>
DATABASE_URI = 'postgresql+psycopg2://'+DB_USERNAME+':'+DB_PASSWORD+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME

db_engine = create_engine(DATABASE_URI, echo=SQLALCHEMY_ECHO, pool_size=DB_CONNECTION_POOL_SIZE, max_overflow=DB_CONNECTION_MAX_OVERFLOW)
magazine_base = declarative_base()


class Engine:
    def __init__(self):
        try:
            session_factory = sessionmaker(bind=db_engine)
            self.Session = scoped_session(session_factory)
            success_logger.info("=====3=====")
            success_logger.info("Engine Object created...")
        except Exception as error:
            error_logger.exception(error)
            raise

    def get_engine_session(self):
        try:
            self.session = self.Session()
            success_logger.info("=====4=====")
            success_logger.info("Session Object created...")
        except Exception as error:
            error_logger.exception(error)
            raise
        return self.session

    def close_session(self, current_session):
        try:
            current_session.close()
            self.Session.remove()
            success_logger.info("=====5=====")
            success_logger.info('Session Object Removed')
        except Exception as error:
            error_logger.exception(error)
            raise
