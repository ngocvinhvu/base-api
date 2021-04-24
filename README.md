# base-api
Base CRUD api.

# Add model

Add machine model.
- create a machine.py file in postgres with content.

```
from sqlalchemy import Column, String

from .base import BaseModel
from ...common.constants import STRING_LENGTH


class Machine(BaseModel):
    __tablename__ = 'machine'

    name = Column(String(STRING_LENGTH['LONG']))
    host_name = Column(String(STRING_LENGTH['LONG']))
```

Add the model name in `postgres/__init__.py`

```
from .base import BaseModel
from .user import User
from .machine import Machine

__all__ = (
    'BaseModel',
    'User',
    'Machine',
)
```

Migrate model: `alembic revision --autogenerate -m "machine"`

Upgrade to database: `alembic upgrade head`