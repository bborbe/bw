os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

users = {}
directories = {}

pkg_apt = {
    'zsh': {},
}

for username, data in node.metadata['users'].items():
    homedir = data.get('home', '/home/{}'.format(username))

    if data.get('deleted', False):
        users[username] = {
            'delete': True,
        }
    else:
        users[username] = {
            'home': homedir,
            'shell': data.get('shell', '/bin/bash'),
            'full_name': data.get('full_name', username),
        }
        directories[homedir] = {
            'mode': '0700',
            'owner': username,
            'group': 'root',
        }
