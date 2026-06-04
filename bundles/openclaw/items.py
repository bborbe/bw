directories = {}
files = {}

openclaw = node.metadata.get('openclaw', {})

if openclaw.get('enabled', False) and openclaw.get('matrix', {}).get('enabled', False):
    user = openclaw.get('user', 'openclaw')
    matrix = openclaw['matrix']
    home = '/home/{}'.format(user)
    openclaw_dir = '{}/.openclaw'.format(home)
    env_file = '{}/.env'.format(openclaw_dir)

    directories[openclaw_dir] = {
        'owner': user,
        'group': user,
        'mode': '0700',
    }

    env_lines = [
        'MATRIX_HOMESERVER={}'.format(matrix['homeserver']),
        'MATRIX_USER_ID={}'.format(matrix['user_id']),
        'MATRIX_PASSWORD={}'.format(matrix['password']),
    ]

    files[env_file] = {
        'owner': user,
        'group': user,
        'mode': '0600',
        'content': '\n'.join(env_lines) + '\n',
        'needs': [
            'directory:{}'.format(openclaw_dir),
        ],
    }
