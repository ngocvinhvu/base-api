import hashlib
import string
import random

from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import Machine


class MachineBL(BaseLogic):

    ACCESS_KEY_LENGTH = 20
    SEED_KEY_LENGTH = 128

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

    def get(self, page, per_page, order, search_text=None, **kwargs):
        matches = self.session.query(Machine)
        pass

    @classmethod
    def get_secret_key(cls, machine):
        string_to_sign = ''.join(
            [machine.access_key, str(machine.tenant_id), machine.created_at.isoformat(),
             machine.seed_key])
        digest = hashlib.sha256(string_to_sign.encode('utf-8')).hexdigest()
        return digest

    @classmethod
    def update_seed_key(cls, machine):
        machine.seed_key = cls.generate_key(cls.SEED_KEY_LENGTH)
        machine.update()
        return machine

    @classmethod
    def generate_key(cls, length):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join((random.choice(letters_and_digits) for i in range(length)))
