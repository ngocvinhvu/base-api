from .base import PublicResource
from ..logics.machine import MachineBL
from ..schemas.machine import CreatingSchema


class MachineResource(PublicResource):
    POST = dict(
        schema=CreatingSchema,
        logic_func='create'
    )
    logic_class = MachineBL

    def post(self, *args, **kwargs):
        pass


RESOURCES = {
    '/machines': MachineResource
}
