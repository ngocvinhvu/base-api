from sqlalchemy import Column, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel
from ...common.constants import STRING_LENGTH


class Directory(BaseModel):
    __table_args__ = (UniqueConstraint('machine_id'),)

    name = Column(String)
    machine_id = Column(String(STRING_LENGTH['UUID4']), ForeignKey('machine.id'), nullable=False)
    machine = relationship('Machine')
