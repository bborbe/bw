if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
pkg_apt = {}
svc_systemd = {}
directories = {}

if node.metadata.get('nginx', {}).get('enabled', False):
    directories['/etc/nginx/sites-enabled'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'purge': True,
    }
    pkg_apt['nginx'] = {
        'installed': True,
    }
    svc_systemd['nginx'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:nginx'],
    }
    for name, data in node.metadata.get('nginx', {}).get('vhosts', {}).items():
        files['/etc/nginx/sites-enabled/{}.conf'.format(name)] = {
            'source': 'vhost.conf',
            'owner': 'root',
            'group': 'root',
            'mode': '0644',
            'context': {
                'port': data.get('port', 80),
                'root': data.get('root', None),
                'locations': data.get('locations', {}),
                'server_names': data.get('server_names', []),
                'indexes': data.get('indexes', []),
            },
            'content_type': 'mako',
            'needs': ['pkg_apt:nginx'],
            'triggers': ['svc_systemd:nginx:restart'],
        }
else:
    files['/etc/nginx/sites-enabled'] = {
        'delete': True,
    }
    pkg_apt['nginx'] = {
        'installed': False,
    }
    svc_systemd['nginx'] = {
        'running': False,
        'enabled': False,
    }
