from flask import request
from flask_restful import Resource

from .base_error import MethodNotAllowed


class BaseResource(Resource):
    GET = dict(
        schema="BaseGettingSchema",
        param_location='args',
        auth_required=False,
        logic_func='get',
        has_file=False,
    )

    def __init__(self):
        def handle_request():
            method_opts = getattr(self, request.method, None)
            if not method_opts:
                raise MethodNotAllowed

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)
