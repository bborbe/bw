if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

actions = {}

actions['locale-gen'] = {
    'command': 'locale-gen',
    'triggered': True,
    'cascade_skip': False,
}

actions['localectl-set-locale'] = {
    'command': 'localectl set-locale LANG=en_US.utf8',
    'triggered': True,
    'cascade_skip': False,
}

files['/etc/default/locale'] = {
    'source': 'locale',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': [
        'action:locale-gen',
        'action:localectl-set-locale',
    ],
}

files['/etc/locale.gen'] = {
    'source': 'locale.gen',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': [
        'action:locale-gen',
        'action:localectl-set-locale',
    ],
}
