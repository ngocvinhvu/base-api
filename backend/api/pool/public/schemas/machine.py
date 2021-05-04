from backend.common.schemas import BaseSchema, StringField


class CreatingSchema(BaseSchema):
    name = StringField(required=True)
    hostname = StringField(required=False)
