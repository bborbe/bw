os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

svc_systemd = {
}

pkg_apt = {
}

if node.metadata.get('networking', {}).get('enabled', False):
    pkg_apt['resolvconf'] = {
        'installed': True,
    }

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
