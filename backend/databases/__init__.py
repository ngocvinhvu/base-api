from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Postgres(object):
    def __init__(self, uri):
        self.uri = uri

        self.engine = None

        self.start_session()

    def setup_engine(self):
        self.engine = create_engine(self.uri)
        return self.engine

    def start_session(self):
        session_factory = sessionmaker(bind=self.engine)
        session = scoped_session(session_factory)
        return session()
