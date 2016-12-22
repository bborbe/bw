os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
if os == 'ubuntu' and release == 'xenial':
    svc_systemd['openvpn'] = {
        'running': node.metadata.get('openvpn', {}).get('enabled', False),
        'enabled': node.metadata.get('openvpn', {}).get('enabled', False),
        'needs': ['pkg_apt:openvpn'],
    }

if os == 'debian' and release == 'jessie':
    for service, data in node.metadata.get('openvpn', {}).get('services', {}).items():
        svc_systemd['openvpn@{}.service'.format(service)] = {
            'running': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
            'enabled': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
            'needs': ['pkg_apt:openvpn'],
        }
