import json


class HTTPError(Exception):
    status_code = 500
    message = 'An unknown error happened.'

    def __init__(self, error_code=None, message=None, payload=None):
        if message:
            self.message = message

        if error_code:
            self.error_code = error_code
        else:
            self.error_code = self.__class__.__name__

        self.payload = payload

    def output(self):
        data = {
            'message': self.message,
            'error': self.status_code
        }
        if self.payload:
            data['payload'] = str(self.payload)

        return data

    def __str__(self):
        return json.dumps(self.output())


class MethodNotAllowedException(HTTPError):
    status_code = 405
    message = 'Method not allowed.'


class UnauthorizedException(HTTPError):
    status_code = 401
    message = 'Unauthorized error.'


class BadRequestParamsException(HTTPError):
    status_code = 400
    message = 'Bad request params.'


class PermissionException(HTTPError):
    status_code = 403
    message = 'Permission Error.'


class ServiceNotAvailableException(HTTPError):
    status_code = 503
    message = 'Service not available.'


class ServerException(HTTPError):
    status_code = 500
    message = 'Server error.'
