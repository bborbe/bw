os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'openvpn': {
        'installed': node.metadata.get('openvpn', {}).get('enabled', False),
    },
}

svc_systemd = {
    'openvpn': {
        'running': node.metadata.get('openvpn', {}).get('enabled', False),
        'enabled': node.metadata.get('openvpn', {}).get('enabled', False),
        'needs': ['pkg_apt:openvpn'],
    },
}
