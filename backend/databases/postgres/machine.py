from sqlalchemy import Column, String

from .base import BaseModel
from ...common.constants import STRING_LENGTH


class Machine(BaseModel):

    name = Column(String(STRING_LENGTH['LONG']))
    host_name = Column(String(STRING_LENGTH['LONG']))