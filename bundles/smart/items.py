if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
files = {}
svc_systemd = {}

pkg_apt['smartmontools'] = {
    'installed': node.metadata.get('smart', {}).get('enabled', False),
}

if node.metadata.get('smart', {}).get('enabled', False):
    files['/etc/smartd.conf'] = {
        'source': 'smartd.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {},
        'needs': ['pkg_apt:smartmontools'],
        'triggers': [
            'svc_systemd:smartd:restart',
        ],
    }
else:
    files['/etc/smartd.conf'] = {
        'delete': True,
    }

svc_systemd['smartd'] = {
    'running': node.metadata.get('smart', {}).get('enabled', False),
    'enabled': node.metadata.get('smart', {}).get('enabled', False),
    'needs': ['pkg_apt:smartmontools'],
}
