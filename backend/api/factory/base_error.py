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


class MethodNotAllowed(HTTPError):
    status_code = 405
    message = 'Method not allowed.'
