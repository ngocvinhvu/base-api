from common import http_status_code


class HTTPException(Exception):
    status_code = http_status_code.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'An unknown error happened.'
