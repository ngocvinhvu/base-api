import uuid

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String, DateTime, Boolean, event
from sqlalchemy.sql import expression

from ...common.constants import STRING_LENGTH

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


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return ''.join('_%s' % c if c.isupper() else c for c in self.__name__).strip('_').lower()

    id = Column(String(STRING_LENGTH['UUID4']), primary_key=True, default=lambda: str(uuid.uuid4()))

    created_at = Column(DateTime, server_default=UtcNow())
    updated_at = Column(DateTime, server_default=UtcNow())

    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime,)


event.listen(BaseModel, 'before_insert', model_oncreate_listener, propagate=True)
event.listen(BaseModel, 'before_update', model_onupdate_listener, propagate=True)
