os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'rsync': {},
    'ssh': {},
}

directories = {
    "/root": {
        'owner': 'root',
        'group': 'root',
        'mode': '0700',
    },
    "/root/.ssh": {
        'owner': 'root',
        'group': 'root',
        'mode': '0700',
    },
}

files = {
    '/root/.ssh/authorized_key': {
        'source': 'authorized_key',
        'content_type': 'mako',
        'mode': '0400',
        'owner': 'root',
        'group': 'root',
        'needs': ['directory:/root/.ssh'],
    },
}
