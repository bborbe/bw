if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
directories = {}

for username, data in node.metadata['users'].items():
    homedir = data.get('home', '/home/{}'.format(username))
    keys = data.get('authorized_keys', {})
    if data.get('enabled', False) and len(keys) > 0:
        directories['{}/.ssh'.format(homedir)] = {
            'mode': '0700',
            'owner': username,
            'group': 'root',
        }
        files['{}/.ssh/authorized_keys'.format(homedir)] = {
            'source': 'authorized_keys',
            'content_type': 'mako',
            'mode': '0400',
            'owner': username,
            'group': 'root',
            'context': {
                'keys': list(keys),
            },
        }
    else:
        files['{}/.ssh/authorized_keys'.format(homedir)] = {
            'delete': True,
        }
