directories = {}
files = {}

hermes = node.metadata.get('hermes', {})
matrix = hermes.get('matrix', {})
user = hermes.get('user', 'hermes')
home = '/home/{}'.format(user)
hermes_dir = '{}/.hermes'.format(home)
env_file = '{}/.env'.format(hermes_dir)

if hermes.get('enabled', False) and matrix.get('enabled', False):
    for field in ('homeserver', 'user_id', 'password'):
        if matrix.get(field) is None:
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
                'MATRIX_USER_ID': matrix['user_id'],
                'MATRIX_PASSWORD': matrix['password'],
            },
        },
        'needs': [
            'directory:{}'.format(hermes_dir),
        ],
    }
else:
    files[env_file] = {
        'delete': True,
    }
