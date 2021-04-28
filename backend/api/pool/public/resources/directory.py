from .base import PublicResource
from ..logics.directory import DirectoryBL
from ..schemas.directory import CreatingSchema


class DirectoryResource(PublicResource):
    POST = dict(
        schema=CreatingSchema,
        logic_func='create'
    )
    logic_class = DirectoryBL

    def post(self, machine_id, *args, **kwargs):
        pass


RESOURCES = {
    '/machines/<string:machine_id>/directory': DirectoryResource
}
