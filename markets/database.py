from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url, connect_args={'check_same_thread': False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def new_session(self):
        return self.SessionLocal()

    def create_database(self, metadata):
        metadata.create_all(self.engine)


@contextmanager
def transaction(db):
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise


@contextmanager
def session(db_factory):
    db = db_factory.new_session()
    try:
        yield db
    finally:
        db.close()
