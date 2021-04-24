from backend.databases import Postgres
from config import PublicApiConfig
from backend.api.factory import Factory

from .resources import RESOURCES

sql_db = Postgres(PublicApiConfig.POSTGRES_URI)

factory = Factory(PublicApiConfig, sql_db=sql_db, resources=RESOURCES)

app = factory.create_app()
