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
    # upstream {} blocks (e.g. load-balanced backends referenced by proxy_pass).
    # Rendered into a single sites-enabled file so nginx loads it inside http{}.
    upstreams = node.metadata.get('nginx', {}).get('upstreams', {})
    if upstreams:
        # Fail fast at compile time (bw test / precommit) on malformed upstream
        # metadata, rather than letting a bad render surface only at nginx reload.
        for up_name, up_servers in upstreams.items():
            if not up_name or not isinstance(up_servers, (list, tuple)) or not up_servers:
                raise Exception(
                    'nginx: upstream {!r} must have a non-empty list of servers'.format(up_name)
                )
        files['/etc/nginx/sites-enabled/upstreams.conf'] = {
            'source': 'upstreams.conf',
            'owner': 'root',
            'group': 'root',
            'mode': '0644',
            'context': {'upstreams': upstreams},
            'content_type': 'mako',
            'needs': ['pkg_apt:nginx'],
            'triggers': ['svc_systemd:nginx:restart'],
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
    # Remove legacy vhost files (e.g. world's `<domain>.conf`) so a bw-managed
    # vhost replaces them instead of duplicating the server_name. Bridge until
    # sites-enabled can be flipped back to purge:True (all vhosts bw-managed).
    for legacy in node.metadata.get('nginx', {}).get('delete_vhosts', []):
        files['/etc/nginx/sites-enabled/{}'.format(legacy)] = {
            'delete': True,
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
