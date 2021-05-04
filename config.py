import os


def _get_env_or_default(var_name, default_val):
    return os.environ.get(var_name) or default_val


class BaseConfig(object):
    WEB_DOMAIN = 'http://localhost'

    ENV = 'dev'

    # POSTGRES
    POSTGRES_URI = 'postgresql+psycopg2://postgres:vccloud123@10.5.90.23:5432/base-api'


class PublicApiConfig(BaseConfig):
    DEBUG = True
    OS_AUTH_URL = _get_env_or_default('OS_AUTH_URL', 'http://172.19.242.10:5000/v3')
    OS_USERNAME = _get_env_or_default('OS_USERNAME', 'admin')
    OS_PASSWORD = _get_env_or_default('OS_PASSWORD', 'V2VsY29tZTEyMw')
    OS_PROJECT_NAME = _get_env_or_default('OS_PROJECT_NAME', 'admin')
    OS_USER_DOMAIN_NAME = _get_env_or_default('OS_USER_DOMAIN_NAME', 'Default')
    OS_PROJECT_DOMAIN_NAME = _get_env_or_default('OS_PROJECT_DOMAIN_NAME', 'Default')
    OS_REGION_NAME = _get_env_or_default('OS_REGION_NAME', 'HaNoi')


config = {
    'development': PublicApiConfig,
    'staging': None,
    'production': None
}
