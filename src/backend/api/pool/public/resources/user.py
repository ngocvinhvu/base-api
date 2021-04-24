from flask import request

from .base import PublicResource
from ..logics.user import UserLogic
from ..schemas.user import UserSchema


class UserResource(PublicResource):
    GET = dict(
        param_location='args',
        auth_required=False,
        logic_func='get',
        has_file=False,
    )

    def get(self):
        """
        Get user info
        ---
        tags:
          - users
        definitions:
          - schema:
            id: Group
        :return:
        """
        pass

    POST = dict(
        schema=UserSchema,
        param_location='json',
        auth_required=False,
        logic_func='post',
        has_file=False,
    )

    def post(self):
        pass

    logic_class = UserLogic


RESOURCES = {
    '/user': UserResource
}
