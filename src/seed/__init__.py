from backend.databases.postgres import *


class Seeder(object):

    def __init__(self, postgres_db):
        self.postgres_db = postgres_db
        self.session = self.postgres_db.start_session()

    def init_db(self):
        pass

    def drop_db(self):
        confirm = input('Are you fucking sure? (y/n): ')
        if confirm.lower() != 'y':
            return
        BaseModel.metadata.drop_all(self.postgres_db.engine)

    def reset_db(self, create_all=False):
        self.drop_db()
        if create_all:
            BaseModel.metadata.create_all(self.postgres_db.engine)

        self.init_db()

    def refresh_session(self):
        self.session.close()
        self.session = self.postgres_db.start_session()
        return self.session
