if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}

files = {}

actions = {
}

if node.metadata.get('grub', {}).get('enabled', False):
    pkg_apt['grub2-common'] = {}

    actions['update-grub'] = {
        'command': 'update-grub',
        'triggered': True,
        'cascade_skip': False,
    }

    name = ''
    if node.os == 'ubuntu':
        name = 'Ubuntu'
    if node.os == 'debian':
        name = 'Debian'
    if len(name) == 0:
        raise Exception('can not find name for grub files')

    files['/etc/default/grub'] = {
        'source': 'default-grub',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'name': name,
            'default': node.metadata.get('grub', {}).get('default', '0'),
            'cmd_args': node.metadata.get('grub', {}).get('cmd_args', {}),
            'serial': node.metadata.get('grub', {}).get('serial', False),
        },
        'triggers': ['action:update-grub'],
        'needs': ['pkg_apt:grub2-common'],
    }
