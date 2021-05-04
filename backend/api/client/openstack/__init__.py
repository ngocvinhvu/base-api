import os

from keystoneauth1.identity import v3
from keystoneauth1.session import Session
from keystoneclient.v3 import client as keystone_client

from config import config

env = os.environ.get('ENV', 'development')
CONF = config[env]


def create_session(tenant_name, token, tenant_id=None):
    d = {'project_name': tenant_name}
    if tenant_id:
        d['project_id'] = tenant_id
    d['project_domain_name'] = CONF.OS_PROJECT_DOMAIN_NAME
    auth = v3.Token(auth_url=CONF.OS_AUTH_URL,
                    token=token, **d)
    return Session(auth=auth)


def create_ks_client(sess):
    return keystone_client.Client(session=sess)


def create_admin_session():
    keystone_authtoken = {
        'auth_url': CONF.OS_AUTH_URL,
        'username': CONF.OS_USERNAME,
        'password': CONF.OS_PASSWORD,
        'project_name': CONF.OS_PROJECT_NAME,
        'user_domain_name': CONF.OS_USER_DOMAIN_NAME,
        'project_domain_name': CONF.OS_PROJECT_DOMAIN_NAME
    }
    auth = v3.Password(**keystone_authtoken)
    return Session(auth=auth)
