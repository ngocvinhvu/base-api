from flask import g, request, jsonify
from flask_restful import Resource

from .base_errors import BadRequestParamException, LogicUnimplementedMethodException, MethodNotAllowedException
from .base_logics import BaseLogic
from ...common.constants import DEFAULT_METHODS_PARAMS_LOCATION
from ...common.schemas import BaseInputSchema


class BaseResource(Resource):
    """
    Class resources extended from BaseResource will be format

    Enable http method, example GET

    GET = dict(
        schema=BaseInputSchema,
        param_location='args',
        auth_required=False,
        logic_func='get',
        has_file=False,
    )
    def get(self):
        pass

    logic_class = LOGIC_CLASS_NAME
    """
    auth_required = False

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
            if not method_opts:
                raise MethodNotAllowedException
            '''TODO Check authentication'''

            '''Get params'''
            try:
                params = self.parse_request_params(method_opts)
            except BadRequestParamException as e:
                resp = jsonify(e.output())
                resp.status_code = e.status_code
                return resp

            logic = self.logic_class(g.session, g.sql)
            logic_func_name = method_opts.get('logic_func', None)
            logic_func = getattr(logic, logic_func_name, None)
            if not logic_func:
                raise LogicUnimplementedMethodException(method=logic_func_name)
            kwargs.update(params)
            return logic_func(*args, **kwargs)

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)

    def parse_request_params(self, method_opts):
        method = request.method

        input_schema = method_opts.get('schema')
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
                raise BadRequestParamException(payload='Required file in body')
            raw_params['file'] = file

        err = input_schema.validate(raw_params)
        if err:
            raise BadRequestParamException(payload=str(err))

        return input_schema.load(raw_params).data

    def handle_auth(self):
        pass


__all__ = (
    'BaseResource'
)
