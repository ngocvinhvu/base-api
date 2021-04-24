from datetime import datetime

from marshmallow import Schema, fields, ValidationError

from .constants import STRING_LENGTH

STRING_LENGTH_VALIDATORS = {
    'SHORT': lambda value: len(value) <= STRING_LENGTH['SHORT'],
    'MEDIUM': lambda value: len(value) <= STRING_LENGTH['MEDIUM'],
    'LONG': lambda value: len(value) <= STRING_LENGTH['LONG'],
    'LARGE': lambda value: len(value) <= STRING_LENGTH['LARGE'],
}


class IdField(fields.Field):
    def _validate(self, value):
        print(value)
        if not isinstance(value, str):
            raise ValidationError('Invalid id.')
        if len(value) != STRING_LENGTH['UUID4']:
            raise ValidationError('Invalid id.')


class DatetimeField(fields.Field):
    def _validate(self, value):
        if not isinstance(value, datetime):
            if isinstance(value, float) or isinstance(value, int):
                try:
                    value = datetime.utcfromtimestamp(value)
                except Exception:
                    raise ValidationError('Invalid datetime!')

        return super()._validate(value)


class ListField(fields.Field):
    pass


class BaseSchema(Schema):
    pass


class BaseInputSchema(BaseSchema):
    pass


class BaseCreatingSchema(BaseInputSchema):
    pass


class BaseGettingSchema(BaseInputSchema):
    id = IdField(required=True)


class BaseUpdatingSchema(BaseInputSchema):
    id = IdField(required=True)
