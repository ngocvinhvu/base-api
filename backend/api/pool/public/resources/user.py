from .base import PublicResource


class UserResource(PublicResource):

    def get(self, *args, **kwargs):
        pass


RESOURCES = {
    '/user': UserResource
}
