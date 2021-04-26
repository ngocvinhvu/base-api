from .base import PublicResource


class User(PublicResource):
    # POST = dict(
    #     schema="CreatingSchema",
    #     logic_func='create'
    # )

    def post(self):
        pass


RESOURCES = {
    '/user': User
}
