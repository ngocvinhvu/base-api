from marshmallow import fields, ValidationError, Schema


class IdField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, str):
            raise ValidationError('Invalid id.')


class StringField(fields.String):
    def _validate(self, value):
        if not isinstance(value, str):
            raise ValidationError('Invalid id.')


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
