os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {
    '/etc/sudoers.d/users': {
        'source': 'users',
        'content_type': 'mako',
        'mode': '0440',
        'owner': 'root',
        'group': 'root',
        'context': {
            'users': node.metadata['users'],
        },
    },
}

pkg_apt = {
    "sudo": {},
}
