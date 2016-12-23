os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

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
        'users': dict((k, v) for k, v in node.metadata['users'].items() if v.get('sudo', False)),
    },
}

pkg_apt = {
    'sudo': {},
}
