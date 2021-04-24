from flask import make_response

from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import User


class UserLogic(BaseLogic):

    def get(self):
        html = """
        """
        resp = make_response(html)
        resp.headers.extend({'content-type': 'text/html; charset=utf-8'})
        return resp

    def post(self, name):
        user = User()
        user.name = name
        self.session.add(user)
        self.session.commit()
        return {'user.id': user.id}
