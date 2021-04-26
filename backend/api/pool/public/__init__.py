from backend.api.factory import Factory
from config import PublicApiConfig

from .resources import RESOURCES

factory = Factory(PublicApiConfig, RESOURCES)

app = factory.create_app()
