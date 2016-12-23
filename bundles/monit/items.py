os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}
svc_systemd = {}

pkg_apt = {
    'monit': {
        'installed': node.metadata.get('monit', {}).get('enabled', False),
    },
}

if os == 'ubuntu' and release == 'xenial':
    svc_systemd['monit'] = {
        'running': node.metadata.get('monit', {}).get('enabled', False),
        'enabled': node.metadata.get('monit', {}).get('enabled', False),
        'needs': ['pkg_apt:monit'],
    }
if os == 'debian' and release == 'jessie':
    svc_systemd['monit'] = {
        'running': node.metadata.get('monit', {}).get('enabled', False),
        'needs': ['pkg_apt:monit'],
    }

if node.metadata.get('monit', {}).get('enabled', False):
    files['/etc/monit/conf.d/free_space.conf'] = {
        'source': 'free_space.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['pkg_apt:monit'],
        'triggers': ['svc_systemd:monit:restart'],
    }
else:
    files['/etc/monit/conf.d/free_space.conf'] = {
        'delete': True,
    }

if node.metadata.get('monit', {}).get('enabled', False):
    files['/etc/monit/conf.d/mailserver.conf'] = {
        'source': 'mailserver.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'needs': ['pkg_apt:monit'],
        'triggers': ['svc_systemd:monit:restart'],
        'context': {
            'recipient': node.metadata.get('monit', {}).get('recipient', ''),
            'sender': node.metadata.get('monit', {}).get('sender', ''),
            'server': node.metadata.get('monit', {}).get('server', ''),
            'port': node.metadata.get('monit', {}).get('port', ''),
            'username': node.metadata.get('monit', {}).get('username', ''),
            'password': node.metadata.get('monit', {}).get('password', ''),
        },
    }
else:
    files['/etc/monit/conf.d/mailserver.conf'] = {
        'delete': True,
    }
