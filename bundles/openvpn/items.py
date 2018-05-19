if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
pkg_apt = {}
svc_systemd = {}

pkg_apt['openvpn'] = {
    'installed': node.metadata.get('openvpn', {}).get('enabled', False),
}
pkg_apt['easy-rsa'] = {
    'installed': node.metadata.get('openvpn', {}).get('enabled', False),
}

if node.metadata.get('openvpn', {}).get('enabled', False):
    svc_systemd['openvpn'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:openvpn'],
    }
else:
    svc_systemd['openvpn'] = {
        'running': False,
        'enabled': False,
    }

for service, data in node.metadata.get('openvpn', {}).get('services', {}).items():
    svc_systemd['openvpn@{}.service'.format(service)] = {
        'running': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
        'enabled': node.metadata.get('openvpn', {}).get('enabled', False) and data.get('enabled', False),
        'needs': ['pkg_apt:openvpn'],
    }

if node.metadata.get('openvpn', {}).get('enabled', False):
    files['/etc/default/openvpn'] = {
        'source': 'openvpn',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'services': node.metadata.get('openvpn', {}).get('services', {}).keys(),
        },
        'triggers': [
            'svc_systemd:openvpn:restart',
            'action:systemd-reload'
        ],
    }
else:
    files['/etc/default/openvpn'] = {
        'delete': True,
    }
