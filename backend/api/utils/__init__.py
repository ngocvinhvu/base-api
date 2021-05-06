from functools import wraps

from flask import g, request, session
from flask import current_app as app
from itsdangerous import BadSignature
from flask_restful import abort

from backend.api.client.openstack import create_session, create_ks_client


def auth_require(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method == 'OPTIONS':
            return f(*args, **kwargs)

        use_token = False
        if session.get('token'):
            g.token = session['token']
            use_token = True
        elif request.headers.get('X-Auth-Token'):
            g.token = request.headers.get('X-Auth-Token')
            use_token = True
        tenant_id = None
        if use_token:
            if session.get('email'):
                g.project_name = session['email']
            elif request.headers.get('X-Tenant-Name'):
                g.project_name = request.headers.get('X-Tenant-Name')
            elif request.headers.get('X-Tenant-Id'):
                tenant_id = request.headers.get('X-Tenant-Id')
            else:
                return abort(401)
        else:
            if 'session' not in request.cookies:
                return abort(401, message="%s" % 'Missing authentication info.')
            try:
                serializer = app.config['COOKIE_SERIALIZER']
                user_info = serializer.loads(request.cookies['session'])
                g.project_name = user_info['tenant_name']
                g.token = user_info['token']
            except BadSignature:
                app.logger.debug('Unable to decrypt Session Cookie value: {}'
                                 .format(request.cookies['session']))
                return abort(401, message="%s" % 'Invalid Session Cookie.')
            except Exception as e:
                app.logger.debug(str(e))
                return abort(401, message=str(e))
        g.username = g.project_name
        g.sess = create_session(tenant_name=g.project_name,
                                token=g.token,
                                tenant_id=tenant_id)
        keystone = create_ks_client(g.sess)
        try:
            token_data = keystone.tokens.get_token_data(g.token)
            g.tenant_id = token_data['token']['project']['id']
            g.user_id = token_data['token']['user']['id']
            kwargs['roles'] = token_data['token']['roles']
            kwargs['tenant_id'] = g.tenant_id
        except Exception as e:
            return abort(401)
        return f(*args, **kwargs)

    return decorated
