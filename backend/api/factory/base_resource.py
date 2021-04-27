from flask import request, jsonify
from flask_restful import Resource

from backend.common.schemas import BaseGettingSchema
from backend.common.constants import DEFAULT_METHODS_PARAM_LOCATION

from .base_error import MethodNotAllowed
from .base_logics import BaseLogic


class BaseResource(Resource):
    GET = dict(
        schema=BaseGettingSchema,
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
                raise MethodNotAllowed

            params = self.parse_request_params(method_opts)

            logic = self.logic_class()
            logic_func_name = method_opts.get('logic_func', None)
            logic_func = getattr(logic, logic_func_name, None)
            if not logic_func:
                raise Exception

            kwargs.update(params)
            result = logic_func(*args, **kwargs)
            status_code = result.get('status_code', None)
            if status_code:
                del result['status_code']
            resp = jsonify(result)
            resp.status_code = status_code if status_code else 200
            return resp

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)

    def parse_request_params(self, method_opts):
        method = request.method

        input_schema = method_opts.get('schema')
        if not input_schema:
            return {}
        input_schema = input_schema()
        param_location = method_opts.get('param_location', DEFAULT_METHODS_PARAM_LOCATION.get(method.lower()))
        if not param_location:
            raise Exception

        param_container = getattr(request, param_location) or {}
        raw_params = {}
        for key in param_container:
            raw_params[key] = param_container.get(key)

        err = input_schema.validate(raw_params)
        if err:
            raise Exception
        return input_schema.load(raw_params)
