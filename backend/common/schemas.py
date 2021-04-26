from marshmallow import Schema


class BaseSchema(Schema):
    pass


class BaseInputSchema(BaseSchema):
    pass


class BaseCreatingSchema(BaseInputSchema):
    pass
