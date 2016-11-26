os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    "cron": {},
}

svc_systemd = {
    "cron": {
        'needs': [
            'pkg_apt:cron',
        ],
    },
}

files = {}

for k, v in node.metadata.get('cron', {}).get('jobs', {}).items():
    files['/etc/cron.d/{}'.format(k)] = {
        'source': "cron_file",
        'content_type': 'mako',
        'context': {'schedule': v},
        'group': 'root',
        'mode': '0644',
        'needs': ['pkg_apt:cron'],
        'owner': 'root',
    }
