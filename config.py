class BaseConfig(object):
    WEB_DOMAIN = 'http://localhost'

    ENV = 'dev'

    # POSTGRES
    POSTGRES_URI = 'postgresql+psycopg2://postgres:vccloud123@10.5.90.23:5432/base-api'


class PublicApiConfig(BaseConfig):
    DEBUG = True
