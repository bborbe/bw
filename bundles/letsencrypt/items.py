os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}
directories = {}
actions = {}
pkg_apt = {}
svc_systemd = {}

actions['letsencrypt_run'] = {
    'command': '/etc/letsencrypt.sh/run.sh',
    'needed_by': ['file:/etc/letsencrypt.sh/run.sh', 'file:/etc/letsencrypt.sh/hook.sh', 'file:/etc/letsencrypt.sh/config.sh'],
    'triggered': True,
    'cascade_skip': False,
}

pkg_apt['nginx'] = {
    'installed': node.metadata.get('letsencrypt', {}).get('enabled', False)
}

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    svc_systemd['nginx'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:nginx', 'file:/etc/nginx/nginx.conf'],
    }
else:
    svc_systemd['nginx'] = {
        'running': False,
        'enabled': False,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    email = node.metadata.get('letsencrypt', {}).get('email', '')
    if len(email) == 0:
        raise Exception('letsencrytp email missing')
    files['/etc/letsencrypt.sh/config.sh'] = {
        'source': 'config.sh',
        'content_type': 'mako',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'context': {
            'email': email,
        },
    }
else:
    files['/etc/letsencrypt.sh/config.sh'] = {
        'delete': True,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    files['/etc/letsencrypt.sh/domains.txt'] = {
        'source': 'domains.txt',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'domains': node.metadata.get('letsencrypt', {}).get('domains', {}),
        },
        'triggers': ['action:letsencrypt_run'],
    }
else:
    files['/etc/letsencrypt.sh/domains.txt'] = {
        'delete': True,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    files['/etc/letsencrypt.sh/hook.sh'] = {
        'source': 'hook.sh',
        'content_type': 'text',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'context': {},
    }
else:
    files['/etc/letsencrypt.sh/hook.sh'] = {
        'delete': True,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    files['/etc/letsencrypt.sh/run.sh'] = {
        'source': 'run.sh',
        'content_type': 'text',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'context': {},
    }
else:
    files['/etc/letsencrypt.sh/run.sh'] = {
        'delete': True,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    directories['/var/www/letsencrypt.sh/.well-known/acme-challenge'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    files['/etc/nginx/nginx.conf'] = {
        'source': 'nginx.conf',
        'content_type': 'text',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {},
        'needs': ['pkg_apt:nginx'],
        'triggers': ['svc_systemd:nginx:restart'],
    }
else:
    files['/etc/nginx/nginx.conf'] = {
        'delete': True,
    }

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    files['/var/www/letsencrypt.sh/.well-known/acme-challenge/letsencrypt.txt'] = {
        'content': 'letsencrypt',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
    }
else:
    files['/var/www/letsencrypt.sh/.well-known/acme-challenge/letsencrypt.txt'] = {
        'delete': True,
    }
