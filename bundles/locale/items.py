os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

actions = {}

actions['locale-gen'] = {
    'command': 'locale-gen',
    'triggered': True,
    'cascade_skip': False,
}

files['/etc/default/locale'] = {
    'source': 'locale',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': ['action:locale-gen'],
}

files['/etc/locale.gen'] = {
    'source': 'locale.gen',
    'content_type': 'mako',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': ['action:locale-gen'],
}
