if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

pkg_apt = {
    'sudo': {},
}

files['/etc/sudoers'] = {
    'source': 'sudoers',
    'content_type': 'text',
    'mode': '0440',
    'owner': 'root',
    'group': 'root',
    'context': {},
}

files['/etc/sudoers.d/users'] = {
    'source': 'users',
    'content_type': 'mako',
    'mode': '0440',
    'owner': 'root',
    'group': 'root',
    'context': {
        'users': dict((k, v) for k, v in node.metadata['users'].items() if v.get('enabled', False) and v.get('sudo', False)),
    },
}

