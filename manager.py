from api.pool.public import app
from flask_script import Manager
from flask_migrate import MigrateCommand

if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command("db", MigrateCommand)
    manager.run()
