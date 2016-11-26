os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

parts = node.hostname.split('.', 2)
if len(parts) == 0:
    raise Exception('invalid hostname {} is missing'.format(hostname))

files = {
    '/etc/hostname': {
        'source': 'hostname',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'hostname': 'fire',
        },
    },
}
