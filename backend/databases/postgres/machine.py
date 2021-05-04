from enum import Enum, unique

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import ENUM, UUID

from .base import BaseModel
from ...common.constants import STRING_LENGTH


@unique
class MachineStatus(Enum):
    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'


class Machine(BaseModel):

    name = Column(String(STRING_LENGTH['LONG']))
    hostname = Column(String(STRING_LENGTH['LONG']))
    status = Column(ENUM(MachineStatus), default=MachineStatus.OFFLINE)
    operation_status = Column(Boolean(), default=True)
    ip_address = Column(String())
    os_version = Column(String)
    agent_version = Column(String)
    access_key = Column(String(20), unique=True)
    seed_key = Column(String(128))
    tenant_id = Column(UUID(as_uuid=True))
