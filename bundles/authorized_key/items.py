os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

for username, data in node.metadata['users'].items():
    keys = data.get('authorized_keys')
    if keys:
        homedir = data.get('home', '/home/{}'.format(username))
        directories = {
            '{}/.ssh'.format(homedir): {
                'mode': '0700',
                'owner': username,
                'group': username,
            },
        }
        files = {
            '{}/.ssh/authorized_keys'.format(homedir): {
                'source': 'authorized_keys',
                'content_type': 'mako',
                'mode': '0400',
                'owner': username,
                'group': username,
                'context': {
                    'keys': list(keys),
                },
            },
        }
