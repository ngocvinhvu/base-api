from .base import PublicResource


class User(PublicResource):
    POST = dict(
        schema="test",
        logic_func='create'
    )

    def get(self):
        return "hello"

    def post(self):
        pass


RESOURCES = {
    '/user': User
}
