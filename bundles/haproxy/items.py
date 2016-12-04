os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'haproxy': {
        'installed': node.metadata.get('haproxy', {}).get('enabled', False),
    },
}

svc_systemd = {
    'haproxy': {
        'running': node.metadata.get('haproxy', {}).get('enabled', False),
        'enabled': node.metadata.get('haproxy', {}).get('enabled', False),
        'needs': ['pkg_apt:haproxy'],
    },
}

files = {
    '/etc/haproxy/haproxy.cfg': {
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
    },
}
