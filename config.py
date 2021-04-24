class BaseConfig(object):
    WEB_DOMAIN = 'http://localhost'

    ENV = 'dev'

    # POSTGRES
    POSTGRES_URI = 'postgresql+psycopg2://postgres:1@localhost:5432/postgres'


class PublicApiConfig(BaseConfig):
    DEBUG = True
