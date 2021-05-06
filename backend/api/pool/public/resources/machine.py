from backend.api.utils import auth_require
from .base import PublicResource
from ..logics.machine import MachineBL
from ..schemas.machine import CreatingSchema, CreatedSchema


class MachineResource(PublicResource):
    POST = dict(
        decorators=[auth_require],
        input_schema=CreatingSchema,
        output_schema=CreatedSchema,
        logic_func='create'
    )
    logic_class = MachineBL

    def post(self, *args, **kwargs):
        pass

    GET = dict(
        decorators=[auth_require],

    )

    def get(self, *args, **kwargs):
        pass


RESOURCES = {
    '/machines': MachineResource
}
