import os

import requests

from backend.common.constants import APP_ROOT_DIR
from backend.databases.postgres import *


class MigrationWorker(object):

    def __init__(self, session):
        self.session = session

    def move_storage(self):
        tmp_dir = os.path.join(APP_ROOT_DIR, 'tmp')

        def run(file, file_type):
            try:
                res = requests.get(file.url)
                print(res)
            except Exception as e:
                print(e)
                return run(file, file_type)
