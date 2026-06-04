directories = {}
files = {}
svc_systemd = {}

hermes = node.metadata.get('hermes', {})
matrix = hermes.get('matrix', {})
brave = hermes.get('brave', {})
user = hermes.get('user', 'hermes')
home = '/home/{}'.format(user)
hermes_dir = '{}/.hermes'.format(home)
credentials_file = '{}/bw-credentials.env'.format(hermes_dir)
service_file = '/etc/systemd/system/hermes.service'

if hermes.get('enabled', False):
    files[service_file] = {
        'source': 'hermes.service',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'user': user,
            'credentials_file': credentials_file,
        },
        'triggers': [
            'action:systemd-reload',
            'svc_systemd:hermes:restart',
        ],
        'needed_by': [
            'svc_systemd:hermes',
        ],
    }
    svc_systemd['hermes'] = {
        'needs': [
            'file:{}'.format(service_file),
        ],
    }
else:
    files[service_file] = {
        'delete': True,
    }
    svc_systemd['hermes'] = {
        'running': False,
        'enabled': False,
    }

env_vars = {}

if hermes.get('enabled', False) and matrix.get('enabled', False):
    for field in ('homeserver', 'user_id', 'password'):
        if not matrix.get(field):
            raise Exception(
                'hermes.matrix.{} required when matrix.enabled on {}'.format(field, node.name)
            )
    env_vars['MATRIX_HOMESERVER'] = matrix['homeserver']
    env_vars['MATRIX_USER'] = matrix['user_id']
    env_vars['MATRIX_PASSWORD'] = matrix['password']

if hermes.get('enabled', False) and brave.get('enabled', False):
    if not brave.get('api_key'):
        raise Exception(
            'hermes.brave.api_key required when brave.enabled on {}'.format(node.name)
        )
    env_vars['BRAVE_SEARCH_API_KEY'] = brave['api_key']

if env_vars:
    directories[hermes_dir] = {
        'owner': user,
        'group': user,
        'mode': '0700',
        'needs': [
            'user:{}'.format(user),
        ],
    }
    files[credentials_file] = {
        'source': 'env',
        'content_type': 'mako',
        'mode': '0600',
        'owner': user,
        'group': user,
        'context': {
            'env': env_vars,
        },
        'needs': [
            'directory:{}'.format(hermes_dir),
        ],
        'triggers': [
            'svc_systemd:hermes:restart',
        ],
    }
else:
    files[credentials_file] = {
        'delete': True,
    }
