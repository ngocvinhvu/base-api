from flask import Flask, jsonify, g
from flask_restful import Api

from backend.api.factory.base_error import HTTPError


class Factory(object):

    def __init__(self, config, sql_db, resources=None):
        self.config = config
        self.sql_db = sql_db
        self.resources = resources

    def create_app(self):
        app = Flask(__name__)

        """Load config"""
        app.config.from_object(self.config)

        """API"""
        api = Api(app)

        @app.before_request
        def handle_before_request():
            g.session = self.sql_db.start_session()
            g.sql = self.sql_db

        @app.after_request
        def handle_after_request(response):
            session = g.session
            g.session = None
            session.close()
            return response

        # Custom Error handling
        @app.errorhandler(HTTPError)
        def handle_invalid_usage(error):
            response = jsonify(error.output())
            response.status_code = error.status_code
            return response

        """RESOURCES installation"""
        for endpoint, resource in self.resources.items():
            api.add_resource(resource, endpoint)

        return app
