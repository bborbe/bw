if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
actions = {}
symlinks = {}

actions['locale-gen'] = {
    'needs': ['pkg_apt:locales'],
    'command': 'locale-gen',
    'triggered': True,
    'cascade_skip': False,
}

actions['localectl-set-locale'] = {
    'command': 'localectl set-locale LANG=en_US.utf8',
    'triggered': True,
    'cascade_skip': False,
}

files['/etc/locale.conf'] = {
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
symlinks['/etc/default/locale'] = {
    'group': 'root',
    'owner': 'root',
    'target': '../locale.conf',
    'needs': ['file:/etc/locale.conf'],
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
