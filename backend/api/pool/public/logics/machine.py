from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import Machine


class MachineBL(BaseLogic):

    def create(self, name, hostname):
        machine = Machine(name=name, hostname=hostname)
        self.session.add(machine)
        # self.session.commit()
        return {
            "status_code": 201,
            "name": machine.name,
            "hostname": machine.hostname,
            "created_at": machine.created_at
        }
