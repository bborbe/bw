files = {}
svc_systemd = {}
pkg_apt = {}

pkg_apt['monit'] = {
    'installed': node.metadata.get('monit', {}).get('enabled', False),
}

svc_systemd['monit'] = {
    'running': node.metadata.get('monit', {}).get('enabled', False),
    'enabled': node.metadata.get('monit', {}).get('enabled', False),
    'needs': ['pkg_apt:monit'],
}

for name, data in node.metadata.get('monit', {}).get('checks', {}).items():
    path = '/etc/monit/conf.d/{name}.conf'.format(name=name)
    if node.metadata.get('monit', {}).get('enabled', False) and data.get('enabled', True):
        files[path] = {
            'source': data.get('template', '{name}.conf'.format(name=name)),
            'content_type': 'mako',
            'mode': '0400',
            'owner': 'root',
            'group': 'root',
            'needs': ['pkg_apt:monit'],
            'triggers': ['svc_systemd:monit:restart'],
            'context': data.get('context', {}),
        }
    else:
        files[path] = {
            'delete': True,
            'triggers': ['svc_systemd:monit:restart'],
        }
