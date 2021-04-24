import os

import config

APP_ROOT_DIR = os.path.dirname(config.__file__)


DATE_FORMAT = '%d/%m/%Y'
DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'


STRING_LENGTH = {
    'UUID4': 36,
    'SHORT': 50,
    'MEDIUM': 200,
    'LONG': 500,
    'LARGE': 3000,
}

DEFAULT_METHODS_PARAMS_LOCATION = {
    'post': 'json',
    'patch': 'json',
    'put': 'json',
    'get': 'args',
    'delete': 'args',
}

