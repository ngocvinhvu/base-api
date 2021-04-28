from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import Machine


class MachineBL(BaseLogic):

    def create(self, name, host_name):
        machine = Machine(name=name, host_name=host_name)
        self.session.add(machine)
        self.session.commit()
        return {
            "status_code": 201,
            "name": machine.name,
            "host_name": machine.host_name,
            "created_at": machine.created_at
        }
