from backend.api.pool.public import app
from flask_script import Manager
from flask_migrate import MigrateCommand

manager = Manager(app)

if __name__ == "__main__":
    manager.add_command('db', MigrateCommand)
    manager.run()
