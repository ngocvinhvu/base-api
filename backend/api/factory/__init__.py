from flask import Flask, jsonify
from flask_restful import Api

from backend.api.factory.base_error import HTTPError


class Factory(object):

    def __init__(self, config, resources=None):
        self.config = config
        self.resources = resources

    def create_app(self):
        app = Flask(__name__)

        """Load config"""
        app.config.from_object(self.config)

        """API"""
        api = Api(app)

        @app.errorhandler(HTTPError)
        def handle_invalid_usage(error):
            response = jsonify(error.output())
            response.status_code = error.status_code
            return response

        """RESOURCES installation"""
        for endpoint, resource in self.resources.items():
            api.add_resource(resource, endpoint)

        return app
