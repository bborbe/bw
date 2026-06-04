directories = {}
files = {}
svc_systemd = {}

hermes = node.metadata.get('hermes', {})
matrix = hermes.get('matrix', {})
user = hermes.get('user', 'hermes')
home = '/home/{}'.format(user)
hermes_dir = '{}/.hermes'.format(home)
env_file = '{}/.env'.format(hermes_dir)
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

if hermes.get('enabled', False) and matrix.get('enabled', False):
    for field in ('homeserver', 'user_id', 'password'):
        if not matrix.get(field):
            raise Exception(
                'hermes.matrix.{} required when matrix.enabled on {}'.format(field, node.name)
            )

    directories[hermes_dir] = {
        'owner': user,
        'group': user,
        'mode': '0700',
        'needs': [
            'user:{}'.format(user),
        ],
    }
    files[env_file] = {
        'source': 'env',
        'content_type': 'mako',
        'mode': '0600',
        'owner': user,
        'group': user,
        'context': {
            'env': {
                'MATRIX_HOMESERVER': matrix['homeserver'],
                'MATRIX_USER': matrix['user_id'],
                'MATRIX_PASSWORD': matrix['password'],
            },
        },
        'needs': [
            'directory:{}'.format(hermes_dir),
        ],
        'triggers': [
            'svc_systemd:hermes:restart',
        ],
    }
else:
    files[env_file] = {
        'delete': True,
    }
