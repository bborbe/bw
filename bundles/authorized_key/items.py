if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

for username, data in node.metadata['users'].items():
    if data.get('enabled', False):
        keys = data.get('authorized_keys', {})
        if len(keys) > 0:
            homedir = data.get('home', '/home/{}'.format(username))
            directories = {
                '{}/.ssh'.format(homedir): {
                    'mode': '0700',
                    'owner': username,
                    'group': 'root',
                },
            }
            files = {
                '{}/.ssh/authorized_keys'.format(homedir): {
                    'source': 'authorized_keys',
                    'content_type': 'mako',
                    'mode': '0400',
                    'owner': username,
                    'group': 'root',
                    'context': {
                        'keys': list(keys),
                    },
                },
            }
