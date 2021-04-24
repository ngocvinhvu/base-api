import uuid
from datetime import datetime

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String, DateTime, Boolean, Integer, event
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import expression
from sqlalchemy.inspection import inspect as sa_inspect

from backend.common.constants import DATE_FORMAT, STRING_LENGTH

Base = declarative_base()


class UtcNow(expression.FunctionElement):
    type = DateTime()


@compiles(UtcNow, 'postgresql')
def get_now(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


def model_oncreate_listener(mapper, connection, instance):
    instance.created_at = UtcNow()
    instance.updated_at = UtcNow()


def model_onupdate_listener(mapper, connection, instance):
    instance.created_at = instance.created_at
    instance.updated_at = UtcNow()
    if instance.deleted is True:
        instance.deleted_at = UtcNow()


class Serializer(object):

    @classmethod
    def parse_value(cls, value):
        if value is None:
            return None
        if isinstance(value, datetime):
            return value.strftime(DATE_FORMAT)
        return value

    def serialize_data(self, **kwargs):
        result = dict()

        all_columns = self.__table__.columns
        for field_name in all_columns.keys():
            raw_data = getattr(self, field_name, None)
            result[field_name] = self.parse_value(raw_data)

        for attr in sa_inspect(self.__class__).all_orm_descriptors:
            if not isinstance(attr, hybrid_property):
                continue
            raw_data = getattr(self, attr.__name__, None)
            result[attr.__name__] = self.parse_value(raw_data)
        return result

    def filter_data(self, data, excludes=None, **kwargs):
        all_keys = set(data.keys())

        result_keys = all_keys.difference(set(excludes or []))
        must_includes = ['id']
        for must_include_key in must_includes:
            if must_include_key in result_keys:
                continue
            result_keys.add(must_include_key)

        all_columns = self.__table__.columns
        for key in all_keys:
            column = all_columns.get(key)
            if column is not None and column.primary_key:
                continue

            if key not in result_keys:
                data.pop(key, None)
        return data

    def output(self, excludes=None, **kwargs):
        data = self.serialize_data(**kwargs)
        result = self.filter_data(data, excludes)
        return result


class BaseModel(Base, Serializer):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return ''.join('_%s' % c if c.isupper() else c
                       for c in self.__name__).strip('_').lower()

    id = Column(String(STRING_LENGTH['UUID4']), primary_key=True, default=lambda: str(uuid.uuid4()))

    created_at = Column(DateTime, server_default=UtcNow())
    updated_at = Column(DateTime, server_default=UtcNow())

    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime,)

    @classmethod
    def convert_from_dict(cls, data, origin=None):
        if origin:
            if not isinstance(origin, cls):
                raise Exception('Invalid origin object of %s.' % cls.__name__)
            result = origin
        else:
            result = cls()
        all_fields = cls.__table__.columns
        for field_name in all_fields.keys():
            value = data.get(field_name)
            if value is None:
                continue
            if value == getattr(result, field_name, None):
                continue
            setattr(result, field_name, value)
        return result


event.listen(BaseModel, 'before_insert', model_oncreate_listener, propagate=True)
event.listen(BaseModel, 'before_update', model_onupdate_listener, propagate=True)
