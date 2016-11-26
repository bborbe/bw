os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'monit': {},
}

svc_systemd = {
    'monit': {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:monit'],
    },
}

files = {
    '/etc/monit/conf.d/free_space.conf': {
        'source': 'free_space.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    },
    '/etc/monit/conf.d/mailserver.conf': {
        'source': 'mailserver.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
    },
}
