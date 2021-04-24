from .base import PublicResource


class User(PublicResource):
    POST = dict(
        schema="test",
        logic_func='post'
    )

    def get(self):
        pass

    def post(self):
        pass


RESOURCES = {
    '/user': User
}
