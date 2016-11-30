os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'docker-engine': {
        'installed': node.metadata.get('docker', False),
    },
    'docker.io': {
        'installed': False,
    },
}
