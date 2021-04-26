from flask_script import Manager

from backend.api.pool.public import app

if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
