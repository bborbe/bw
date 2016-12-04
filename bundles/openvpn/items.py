os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'openvpn': {
        'installed': node.metadata.get('openvpn', False),
    },
}

svc_systemd = {
    "openvpn": {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openvpn'],
    },
}
