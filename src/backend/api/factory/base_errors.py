import json

from backend.common import http_status_code
from backend.common.utils import log


class HTTPException(Exception):
    status_code = http_status_code.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'An unknown error happened.'

    def __init__(self, message=None, error_code=None, payload=None, **kwargs):
        self.kwargs = kwargs
        self.kwargs['message'] = message

        if 'status_code' not in self.kwargs:
            try:
                self.kwargs['status_code'] = self.status_code
            except AttributeError:
                pass

        if error_code:
            self.error_code = error_code
        else:
            self.error_code = self.__class__.__name__

        if self._should_format():
            try:
                message = self.message % kwargs
            except Exception:
                self._log_exception()
                message = self.message
        self.msg = message
        self.payload = payload
        super(HTTPException, self).__init__(message)
        self.kwargs.pop('message', None)

    def _log_exception(self):
        # kwargs doesn't match a variable in the message
        # Log the issue and the kwargs
        log.exception('Exception in string format operation:')
        for name, value in self.kwargs.items():
            log.error('%(name)s: %(value)s', {'name': name, 'value': value})

    def _should_format(self):
        return self.kwargs['message'] is None or '%(message)' in self.message

    def output(self):
        data = {
            'message': self.msg,
            'error': self.error_code
        }
        if self.payload:
            data['payload'] = str(self.payload)
        return data

    def __str__(self):
        return json.dumps(self.output())


class LogicUnimplementedMethodException(HTTPException):
    """
    Logic class not implement method in dict
    """
    status_code = http_status_code.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Logic Unimplemented method %(method)s'


class BadRequestParamException(HTTPException):
    status_code = http_status_code.HTTP_400_BAD_REQUEST
    message = 'Bad request params.'


class MethodNotAllowedException(HTTPException):
    status_code = http_status_code.HTTP_405_METHOD_NOT_ALLOWED
    message = 'Method not allowed'
