if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

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
