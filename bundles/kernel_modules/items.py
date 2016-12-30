os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
