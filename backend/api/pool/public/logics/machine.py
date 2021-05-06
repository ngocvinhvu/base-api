import hashlib
import os
import string
import random

from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import Machine
from config import config

ENV = os.environ.get('ENV', 'development')
CONF = config[ENV]


class MachineBL(BaseLogic):
    ACCESS_KEY_LENGTH = 20
    SEED_KEY_LENGTH = 128

    def create(self, name, tenant_id, hostname=None, *args, **kwargs):
        machine = Machine(name=name, hostname=hostname, tenant_id=tenant_id)
        machine.access_key = self.generate_key(self.ACCESS_KEY_LENGTH).upper()
        machine.seed_key = self.generate_key(self.SEED_KEY_LENGTH)
        self.session.add(machine)
        self.session.commit()
        result = machine.output(excludes=['seed_key'])
        result['secret_key'] = self.get_secret_key(machine)
        result['file_content'] = self.gen_config_file(machine)
        result['status_code'] = 201
        return result

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

    @classmethod
    def gen_config_file(cls, machine):
        file_content = dict(
            machine_id=machine.id,
            access_key=machine.access_key,
            secret_key=cls.get_secret_key(machine),
            api_url=CONF.API_URL,
        )
        return file_content
