DATE_FORMAT = '%d/%m/%Y'
DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'

VALID_DATETIME_FORMATS = [
    DATE_FORMAT,
    DATETIME_FORMAT
]

PAGINATION = {
    'page': 1,
    'per_page': 50
}

DEFAULT_METHODS_PARAM_LOCATION = {
    'post': 'json',
    'patch': 'json',
    'put': 'json',
    'get': 'args',
    'delete': 'args',
}

STRING_LENGTH = {
    'UUID4': 36,
    'SHORT': 50,
    'MEDIUM': 200,
    'LONG': 500,
    'LARGE': 3000,
}
