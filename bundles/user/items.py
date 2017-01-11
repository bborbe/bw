if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

users = {}
directories = {}

pkg_apt = {
    'zsh': {},
}

for username, data in node.metadata.get('users', {}).items():
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
            'groups': data.get('groups', []),
        }
        directories[homedir] = {
            'mode': '0700',
            'owner': username,
            'group': 'root',
        }
