os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    "cron": {},
}

svc_systemd = {
    "cron": {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:cron'],
    },
}

files = {}

for name, data in node.metadata.get('cron', {}).get('jobs', {}).items():
    if data.get('enabled', False):
        files['/etc/cron.d/{}'.format(name)] = {
            'source': "cron_file",
            'content_type': 'mako',
            'context': {
                'shell': data.get('shell', '/bin/sh'),
                'path': data.get('path', '/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin'),
                'schedule': data.get('schedule', '* * * * *'),
                'user': data.get('user', 'root'),
                'expression': data.get('expression', '')
            },
            'group': 'root',
            'mode': '0644',
            'needs': ['pkg_apt:cron'],
            'owner': 'root',
        }
    else:
        files['/etc/cron.d/{}'.format(name)] = {
            'delete': True,
        }
