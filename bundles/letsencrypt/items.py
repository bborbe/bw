if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

groups = {}
pkg_apt = {}
files = {}
directories = {}
users = {}

if node.metadata.get('letsencrypt', {}).get('enabled', False):
    directories['/etc/letsencrypt'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }
    directories['/etc/letsencrypt/archive'] = {
        'mode': '0750',
        'owner': 'root',
        'group': 'letsencypt',
        'needs': ['group:letsencypt'],
    }
    directories['/etc/letsencrypt/live'] = {
        'mode': '0750',
        'owner': 'root',
        'group': 'letsencypt',
        'needs': ['group:letsencypt'],
    }
    users['docker-registry'] = {
        'groups': ['letsencypt'],
    }
    groups['letsencypt'] = {
        'delete': False,
    }
    files['/etc/letsencrypt/acme-dns-auth.py'] = {
        'source': 'acme-dns-auth.py',
        'content_type': 'mako',
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
    }
else:
    groups['letsencypt'] = {
        'delete': True,
    }
    files['/etc/letsencrypt/acme-dns-auth.py'] = {
        'delete': True,
    }
