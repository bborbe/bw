directories = {}
files = {}

openclaw = node.metadata.get('openclaw', {})
matrix = openclaw.get('matrix', {})
user = openclaw.get('user', 'openclaw')
home = '/home/{}'.format(user)
openclaw_dir = '{}/.openclaw'.format(home)
env_file = '{}/.env'.format(openclaw_dir)

if openclaw.get('enabled', False) and matrix.get('enabled', False):
    for field in ('homeserver', 'user_id', 'password'):
        if matrix.get(field) is None:
            raise Exception(
                'openclaw.matrix.{} required when matrix.enabled on {}'.format(field, node.name)
            )

    directories[openclaw_dir] = {
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
                'MATRIX_USER_ID': matrix['user_id'],
                'MATRIX_PASSWORD': matrix['password'],
            },
        },
        'needs': [
            'directory:{}'.format(openclaw_dir),
        ],
    }
else:
    files[env_file] = {
        'delete': True,
    }
