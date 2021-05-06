from backend.common.schemas import BaseSchema, StringField, EnumField, BooleanField, IdField, BaseGettingSchema, \
    NestedField
from backend.databases.postgres.machine import MachineStatus


class CreatingSchema(BaseSchema):
    name = StringField(required=True)
    hostname = StringField(allow_none=True)


class ConfigFileSchema(BaseSchema):
    access_key = StringField(required=True)
    api_url = StringField(required=True)
    machine_id = IdField(required=True)
    secret_key = StringField(required=True)


class CreatedSchema(BaseGettingSchema):
    name = StringField()
    hostname = StringField()
    status = EnumField(MachineStatus)
    operation_status = BooleanField()
    ip_address = StringField()
    os_version = StringField()
    agent_version = StringField()
    access_key = StringField()
    secret_key = StringField()
    tenant_id = IdField()
    file_content = NestedField(ConfigFileSchema())


