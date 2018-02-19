if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

pkg_apt = {
    'openvpn': {
        'installed': node.metadata.get('openvpn', {}).get('enabled', False),
    },
    'easy-rsa': {
        'installed': node.metadata.get('openvpn', {}).get('enabled', False),
    },
}

svc_systemd = {}
if node.os == 'ubuntu':
    svc_systemd['openvpn'] = {
        'running': node.metadata.get('openvpn', {}).get('enabled', False),
        'enabled': node.metadata.get('openvpn', {}).get('enabled', False),
        'needs': ['pkg_apt:openvpn'],
    }

if node.os == 'debian':
    for service, data in node.metadata.get('openvpn', {}).get('services', {}).items():
        svc_systemd['openvpn@{}.service'.format(service)] = {
            'running': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
            'enabled': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
            'needs': ['pkg_apt:openvpn'],
        }
