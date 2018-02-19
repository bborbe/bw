if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {
    '/etc/modules': {
        'source': 'modules',
        'content_type': 'mako',
        'context': {
            'modules': node.metadata.get('kernel_modules', {}),
        },
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
    },
}
