if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
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
