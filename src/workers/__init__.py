import threading
import time

import click

from backend.databases import Postgres
from backend.databases import postgres as postgres_models
from config import BaseConfig


@click.group()
def cli():
    pass


@cli.command(short_help='Get Users ')
def get_users():
    postgres_db = Postgres(uri=BaseConfig.POSTGRES_URI)

    while True:
        print('Length thread: %s' % len(threading.enumerate()))
        for t in threading.enumerate():
            print('for thread name: %s' % t.getName())
        session = postgres_db.start_session()
        thread = MessageThread(session)
        thread.start()
        time.sleep(3)


class MessageThread(threading.Thread):

    def __init__(self, session):
        threading.Thread.__init__(self)
        self.session = session

    def run(self):
        print('Thread run name: %s' % self.getName())
        time.sleep(5)
        users = self.session.query(postgres_models.User).all()
        self.session.close()
        for u in users:
            print('User %s, name %s' % (u.id, u.name))
        time.sleep(5)
        print('MessageThread %s exit' % self.getName())
