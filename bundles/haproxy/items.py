if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {}
files = {}
pkg_apt = {}
directories = {}

pkg_apt['haproxy'] = {
    'installed': node.metadata.get('haproxy', {}).get('enabled', False),
}

if node.metadata.get('haproxy', {}).get('enabled', False):
    svc_systemd['haproxy'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:haproxy', 'file:/etc/haproxy/haproxy.cfg', 'directory:/etc/haproxy/ssl'],
    }
else:
    svc_systemd['haproxy'] = {
        'running': False,
        'enabled': False,
    }

if node.metadata.get('haproxy', {}).get('enabled', False):
    files['/etc/haproxy/haproxy.cfg'] = {
        'source': 'haproxy.cfg',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'ip': node.metadata.get('haproxy', {}).get('ip', ''),
        },
        'needs': ['pkg_apt:haproxy'],
        'triggers': ['svc_systemd:haproxy:restart'],
    }
else:
    files['/etc/haproxy/haproxy.cfg'] = {
        'delete': True,
    }

if node.metadata.get('haproxy', {}).get('enabled', False):
    directories['/etc/haproxy/ssl'] = {
        'mode': '0700',
        'owner': 'root',
        'group': 'root',
    }
