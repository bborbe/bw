os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

actions = {}

actions['timedatectl-set-timezone'] = {
    'command': 'timedatectl set-timezone UTC',
    'triggered': True,
    'cascade_skip': False,
}

files['/etc/timezone'] = {
    'source': 'timezone',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': [
        'action:timedatectl-set-timezone',
    ],
}
