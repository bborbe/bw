os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {
    '/etc/default/locale': {
        'source': 'locale',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    },
    '/etc/locale.gen': {
        'source': 'locale.gen',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    },
}
