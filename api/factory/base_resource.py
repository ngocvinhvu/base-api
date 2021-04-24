from flask_restful import Resource
from flask import g, request

from common.constants import DEFAULT_METHODS_PARAMS_LOCATION
from common.schemas import BaseInputSchema

from .base_logic import BaseLogic


class BaseResource(Resource):
    GET = dict(
        schema=BaseInputSchema,
        param_location='args',
        auth_required=False,
        logic_func='get',
        has_file=False,
    )

    logic_class = BaseLogic

    def __init__(self):
        def handle_request(*args, **kwargs):
            method_opts = getattr(self, request.method, None)

            params = self.parse_request_params(method_opts)
            print("param", params)
            # TODO implement Exception
            if not method_opts:
                raise Exception
            logic = self.logic_class(g.session, g.sql)
            logic_func_name = method_opts.get('logic_func', None)
            logic_func = getattr(logic, logic_func_name, None)
            # TODO implement Exception not logic_func
            if not logic_func:
                raise Exception
            kwargs.update(params)
            return logic_func(*args, **kwargs)

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)

    def parse_request_params(self, method_opts):
        method = request.method

        input_schema = method_opts.get('schema', None)
        if not input_schema:
            return {}

        input_schema = input_schema()
        params_location = method_opts.get('param_location', DEFAULT_METHODS_PARAMS_LOCATION.get(method.lower()))
        param_container = getattr(request, params_location) or {}

        raw_params = {}
        for key in param_container:
            raw_params[key] = param_container.get(key)

        if method_opts.get('has_file'):
            file = request.files.get('file')
            if not file:
                # raise BadRequestParamException(payload='Required file in body')
                raise Exception
            raw_params['file'] = file

        err = input_schema.validate(raw_params)
        if err:
            raise Exception
        return input_schema.load(raw_params).data


__all__ = (
    'BaseResource'
)
