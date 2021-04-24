from marshmallow import fields

from backend.common.schemas import BaseCreatingSchema


class UserSchema(BaseCreatingSchema):
    name = fields.String(required=True)
