from api.factory import Factory

from .resources import RESOURCES

factory = Factory("config", "postgres", resources=RESOURCES)

app = factory.create_app()
