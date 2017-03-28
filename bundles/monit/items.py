files = {}
svc_systemd = {}
pkg_apt = {}
directories = {}

pkg_apt['monit'] = {
    'installed': node.metadata.get('monit', {}).get('enabled', False),
}

if node.os == 'debian':
    svc_systemd['monit'] = {
        'running': node.metadata.get('monit', {}).get('enabled', False),
        'needs': ['pkg_apt:monit'],
    }
else:
    svc_systemd['monit'] = {
        'running': node.metadata.get('monit', {}).get('enabled', False),
        'enabled': node.metadata.get('monit', {}).get('enabled', False),
        'needs': ['pkg_apt:monit'],
    }

directories['/etc/monit/conf.d'] = {
    'mode': '0700',
    'owner': 'root',
    'group': 'root',
    'purge': True,
}

if node.metadata.get('monit', {}).get('enabled', False):
    files['/etc/monit/monitrc'] = {
        'source': 'monitrc',
        'content_type': 'mako',
        'mode': '0400',
        'owner': 'root',
        'group': 'root',
        'needs': ['pkg_apt:monit'],
        'triggers': ['svc_systemd:monit:restart'],
        'context': {
            'password': node.metadata.get('monit', {}).get('password', ''),
        },
    }
else:
    files['/etc/monit/monitrc'] = {
        'delete': True,
        'triggers': ['svc_systemd:monit:restart'],
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
