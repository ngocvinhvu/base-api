from backend.common.schemas import BaseSchema, StringField


class CreatingSchema(BaseSchema):
    email = StringField(required=True)
