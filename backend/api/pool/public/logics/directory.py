from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import Directory


class DirectoryBL(BaseLogic):

    def create(self, name, machine_id):
        dir = Directory(name=name, machine_id=machine_id)
        self.session.add(dir)
        self.session.commit()
        return {
            "status_code": 201,
            "name": dir.name,
            "host_name": dir.machine_id,
            "created_at": dir.created_at
        }
