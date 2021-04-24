from flask import Flask
from flask_restful import Api


class Factory(object):

    def __init__(self, config, resources=None):
        self.config = config
        self.resources = resources

    def create_app(self):
        app = Flask(__name__)

        """Load Config"""
        app.config.from_object(self.config)

        """API"""
        api = Api(app)

        """RESOURCES installation"""
        for endpoint, resource in self.resources.items():
            api.add_resource(resource, endpoint)

        return app
