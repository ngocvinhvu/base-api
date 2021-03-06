from flask import request, jsonify, g
from flask_restful import Resource

from backend.common.schemas import BaseGettingSchema
from backend.common.constants import DEFAULT_METHODS_PARAM_LOCATION

from .base_error import MethodNotAllowedException, BadRequestParamsException
from .base_logics import BaseLogic


class BaseResource(Resource):
    GET = dict(
        decorators=[],
        input_schema=BaseGettingSchema,
        output_schema=BaseGettingSchema,
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

            # Get sql_session and sql.
            sql_session = g.session
            sql = g.sql

            # Get logic function.
            logic = self.logic_class(sql_session, sql)
            logic_func_name = method_opts.get('logic_func', None)
            logic_func = getattr(logic, logic_func_name, None)
            if not logic_func:
                raise NotImplementedError('%s does not have function %s' % (self.logic_class.__name__,
                                                                            logic_func_name))
            decorators = method_opts.get('decorators', [])
            for d in decorators:
                logic_func = d(logic_func)

            # Handle input data.
            params = self.parse_request_params(method_opts)
            kwargs.update(params)

            # Do logic.
            result = logic_func(*args, **kwargs)
            return self.make_response(result, method_opts)

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)

    def parse_request_params(self, method_opts):
        method = request.method

        input_schema = method_opts.get('input_schema')
        if not input_schema:
            return {}
        input_schema = input_schema()
        param_location = method_opts.get('param_location', DEFAULT_METHODS_PARAM_LOCATION.get(method.lower()))
        if not param_location:
            raise NotImplementedError('Missing %s param location!' % method)

        param_container = getattr(request, param_location) or {}
        raw_params = {}
        for key in param_container:
            raw_params[key] = param_container.get(key)

        data, err = input_schema.load(raw_params)
        if err:
            raise BadRequestParamsException(message=str(err))
        return data

    @classmethod
    def make_response(cls, data, method_opts):
        status_code = data.get('status_code', None)
        if status_code:
            del data['status_code']
        status_code = status_code if status_code else 200
        output_schema = method_opts.get('output_schema', None)

        message = output_schema().dump(data).data if output_schema else data
        resp = jsonify(message)
        resp.status_code = status_code
        return resp
