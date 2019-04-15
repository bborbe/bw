if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

files['/etc/modules'] = {
    'source': 'modules',
    'content_type': 'mako',
    'context': {
        'modules': node.metadata.get('kernel_modules', {}),
    },
    'owner': 'root',
    'group': 'root',
    'mode': '0644',
}

files['/etc/modprobe.d/blacklist.conf'] = {
    'source': 'blacklist.conf',
    'content_type': 'text',
    'owner': 'root',
    'group': 'root',
    'mode': '0644',
}
