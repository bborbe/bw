if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

users = {}
directories = {}

pkg_apt = {}

for username, data in node.metadata.get('users', {}).items():
    if 'enabled' in data:
        if data.get('enabled', False):
            homedir = data.get('home', '/home/{}'.format(username))
            users[username] = {
                'home': homedir,
                'shell': data.get('shell', '/bin/bash'),
                'full_name': data.get('full_name', username),
            }
            if len(data.get('groups', [])) > 0:
                users[username]['groups'] = data.get('groups', [])
            for field in ['password', 'salt', 'uid']:
                if field in data:
                    users[username][field] = data[field]
            directories[homedir] = {
                'mode': '0700',
                'owner': username,
                'group': 'root',
            }
            if data.get('generate_password', False):
                users[username]['password'] = repo.vault.password_for('user {user} node {node}'.format(user=username, node=node.name), length=16)
        else:
            users[username] = {
                'delete': True,
            }
