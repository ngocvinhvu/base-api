from config import PublicApiConfig
from backend.api.factory import Factory

from .resources import RESOURCES

factory = Factory(
    config=PublicApiConfig,
    resources=RESOURCES
)

app = factory.create_app()
