from flask import Flask
from flask_restful import Api


class Factory(object):

    def __init__(self,
                 config,
                 sql_db,
                 resources=None,
                 app_name=None,
                 error_handler=None,
                 request_callback=None,
                 response_callback=None):
        self.config = config
        self.sql_db = sql_db
        self.resources = resources or {}
        self.app_name = app_name or 'Flask'
        self.error_handler = error_handler
        self.request_callback = request_callback
        self.response_callback = response_callback

    @staticmethod
    def handle_error(request, error):
        status_code = 500

    def create_app(self):
        app = Flask(__name__)

        api = Api(app)
        for endpoint, resource in self.resources.items():
            api.add_resource(resource, endpoint)
        return app
