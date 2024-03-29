if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
svc_systemd = {}
directories = {}

if node.metadata.get('nginx', {}).get('enabled', False):
    directories['/etc/nginx/sites-enabled'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'purge': False,  # set true again if all vhosts are managed by bw
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
                'ip': data.get('ip', ''),
                'root': data.get('root', None),
                'locations': data.get('locations', {}),
                'server_names': data.get('server_names', []),
                'indexes': data.get('indexes', []),
                'ssl': data.get('ssl', {}),
            },
            'content_type': 'mako',
            'needs': ['pkg_apt:nginx'],
            'triggers': ['svc_systemd:nginx:restart'],
        }
else:
    files['/etc/nginx/sites-enabled'] = {
        'delete': True,
    }
    svc_systemd['nginx'] = {
        'running': False,
        'enabled': False,
    }
