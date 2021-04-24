import os

from flask import Flask, request, jsonify
from flask import g
from flask_restful import Api
from flasgger import Swagger


class Factory(object):

    def __init__(self, config,
                 sql_db,
                 resources=None):
        self.config = config
        self.sql_db = sql_db
        self.resources = resources

    def create_app(self):
        app = Flask(__name__)

        """Load config"""
        app.config.from_object(self.config)

        """API"""
        api = Api(app)

        """Callback before request"""

        @app.before_request
        def handle_before_request():
            g.session = self.sql_db.start_session()
            g.sql = self.sql_db

        """Callback after request"""

        @app.after_request
        def handle_after_request(response):
            session = g.session
            g.session = None
            session.close()
            return response

        """RESOURCES installation"""
        for endpoint, resource in self.resources.items():
            api.add_resource(resource, endpoint)

        '''Register swagger /apidocs'''
        Swagger(app)
        return app
