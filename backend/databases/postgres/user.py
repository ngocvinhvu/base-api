from sqlalchemy import Column, String

from .base import BaseModel
from ...common.constants import STRING_LENGTH


class User(BaseModel):
    status = Column(String(STRING_LENGTH['SHORT']),
                    default='active', index=True)

    avatar_url = Column(String(STRING_LENGTH['LARGE']))

    # for migration
    old_id = Column(String(STRING_LENGTH['LONG']))
