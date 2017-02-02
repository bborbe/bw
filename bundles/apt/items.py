if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'apt-transport-https': {},
    'aptitude': {},
}

actions = {}

files = {}

actions['apt_update'] = {
    'command': 'apt-get update',
    'needed_by': ['pkg_apt:'],
    'triggered': True,
    'cascade_skip': False,
}

for name, data in node.metadata.get('apt', {}).get('repos', {}).items():
    if data['installed']:
        actions['add_gpg_key_{}'.format(data['gpg_key'])] = {
            'command': 'apt-key adv --keyserver keyserver.ubuntu.com --recv-keys {}'.format(data['gpg_key']),
            'unless': 'apt-key list | grep {}'.format(data['gpg_key']),
            'cascade_skip': False,
            'needed_by': ['action:apt_update'],
        }
        files['/etc/apt/sources.list.d/{}.list'.format(name)] = {
            'source': 'source.list',
            'content_type': 'mako',
            'mode': '0644',
            'owner': 'root',
            'group': 'root',
            'context': {
                'lines': data['sources'],
            },
            'needs': ['action:add_gpg_key_{}'.format(data['gpg_key'])],
            'triggers': ['action:apt_update'],
        }
    else:
        files['/etc/apt/sources.list.d/{}.list'.format(name)] = {
            'delete': not data['installed'],
            'triggers': ['action:apt_update'],
        }

for name, data in node.metadata.get('apt', {}).get('packages', {}).items():
    pkg_apt[name] = data
