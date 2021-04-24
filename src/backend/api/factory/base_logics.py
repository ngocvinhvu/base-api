

class BaseLogic(object):

    def __init__(self, session, sql):
        self.session = session
        self.sql = sql

    def get(self, *args, **kwargs):
        return kwargs
