if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'docker-engine': {
        'installed': node.metadata.get('docker', {}).get('enabled', False),
    },
    'docker.io': {
        'installed': False,
    },
}

svc_systemd = {
    'docker': {
        'running': node.metadata.get('docker', {}).get('enabled', False),
        'enabled': node.metadata.get('docker', {}).get('enabled', False),
        'needs': ['pkg_apt:docker-engine'],
    },
}
