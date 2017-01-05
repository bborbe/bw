if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}

svc_systemd = {}

pkg_apt = {}

pkg_apt['resolvconf'] = {
    'installed': False,
}

if node.metadata.get('networking', {}).get('enabled', False):
    svc_systemd['networking'] = {
        'triggered': True,
        'cascade_skip': False,
    }

    files['/etc/network/interfaces'] = {
        'source': 'interfaces',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'interfaces': node.metadata.get('networking', {}).get('interfaces', {}),
            'routes': node.metadata.get('networking', {}).get('routes', {}),
        },
        'triggers': ['svc_systemd:networking:restart'],
    }

    files['/etc/resolv.conf'] = {
        'source': 'resolv.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'nameservers': node.metadata.get('networking', {}).get('nameservers', []),
        },
    }
