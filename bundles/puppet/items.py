if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'puppet': {
        'installed': node.metadata.get('puppet', False),
    },
}
