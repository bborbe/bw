os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'docker-engine': {
        'installed': node.metadata.get('docker', {}).get('enabled', False),
    },
    'docker.io': {
        'installed': False,
    },
}

svc_systemd = {
    "docker": {
        'running': node.metadata.get('docker', {}).get('enabled', False),
        'enabled': node.metadata.get('docker', {}).get('enabled', False),
        'needs': ['pkg_apt:docker-engine'],
    },
}
