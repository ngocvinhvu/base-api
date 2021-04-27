from .base import PublicResource
from ..logics.user import UserBL
from ..schemas.user import CreatingSchema


class UserResource(PublicResource):
    POST = dict(
        schema=CreatingSchema,
        logic_func='create'
    )
    logic_class = UserBL

    def post(self, *args, **kwargs):
        pass


RESOURCES = {
    '/user': UserResource
}
