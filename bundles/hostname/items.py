os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

parts = node.hostname.split('.', 1)
if len(parts) != 2:
    raise Exception('invalid hostname {}'.format(node.hostname))

files = {}

files['/etc/hostname'] = {
    'source': 'hostname',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {
        'hostname': parts[0],
    },
}

files['/etc/hosts'] = {
    'source': 'hosts',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'context': {
        'hostname': parts[0],
        'fqdn': node.hostname,
    },
}
