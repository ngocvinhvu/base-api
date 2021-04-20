from flask_restful import Resource
from flask import request
from sanic.views import HTTP_METHODS


class BaseResource(Resource):

    GET = dict(
        schema="schema get"
    )

    def __init__(self):
        # for http_method in HTTP_METHODS:
        #     def hanle_request():
        #         method_ops = getattr(self, request, None)
        #         print(method_ops)
        def handle_request():
            method_ops = getattr(self, request.method, None)
            print(request)
            print(method_ops)

        handle_request.__name__ = request.method.lower()
        setattr(self, request.method.lower(), handle_request)
    pass


__all__ = (
    'BaseResource'
)
