from backend.common.schemas import BaseSchema, StringField


class CreatingSchema(BaseSchema):
    name = StringField(required=True)
    hostname = StringField(required=False)
    status = EnumField(Machine_Status)
    operation_status = fields.Boolean(dump_only=True)
    ip_address = fields.String()
    os_version = fields.String()
    agent_version = fields.String()
    encryption = fields.Boolean()
    tenant_id = fields.UUID(dump_only=True)
