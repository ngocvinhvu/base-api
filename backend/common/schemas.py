from marshmallow import fields, Schema
from marshmallow_enum import EnumField as LibEnumField


class IdField(fields.UUID):
    pass


class DateTimeField(fields.DateTime):
    pass


class BooleanField(fields.Boolean):
    pass


class EnumField(LibEnumField):
    pass


class StringField(fields.String):
    pass


class NestedField(fields.Nested):
    pass


class BaseSchema(Schema):
    pass


class BaseInputSchema(BaseSchema):
    pass


class BaseCreatingSchema(BaseInputSchema):
    pass


class BaseUpdatingSchema(BaseInputSchema):
    pass


class BaseGettingSchema(BaseInputSchema):
    id = IdField(required=True)

    created_at = DateTimeField()
    updated_at = DateTimeField()
    deleted_at = DateTimeField()
    deleted = BooleanField()
