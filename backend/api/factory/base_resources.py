from flask import request
from flask_restful import Resource

from .base_logics import BaseLogic
from ...common.constants import DEFAULT_METHODS_PARAM_LOCATION


class BaseResource(Resource):
    GET = dict(
        schema="BaseInputSchema",
        param_location='args',
        auth_required=False,
        logic_func='get',
        has_file=False,
    )

    logic_class = BaseLogic

    def __init__(self):
        def handle_request(*args, **kwargs):
            method_opts = getattr(self, request.method, None)
            if not method_opts:
                raise Exception

            params = self.parse_params_request(method_opts)

            logic = self.logic_class()
            logic_func_name = method_opts.get('logic_func', None)
            logic_func = getattr(logic, logic_func_name, None)
            if not logic_func:
                raise Exception

            kwargs.update(params)
            return logic_func(*args, **kwargs)

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)

    def parse_params_request(self, method_opts):
        method = request.method

        param_location = method_opts.get('param_location', DEFAULT_METHODS_PARAM_LOCATION.get(method.lower()))

        if not param_location:
            raise Exception('Missing params')

        param_container = getattr(request, param_location) or {}

        return param_container


__all__ = (
    'BaseResource'
)
