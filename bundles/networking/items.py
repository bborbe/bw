if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
svc_systemd = {}
pkg_apt = {}

if node.metadata.get('networking', {}).get('enabled', False):
    pkg_apt['resolvconf'] = {
        'installed': False,
    }
    pkg_apt['network-manager'] = {
        'installed': False,
    }
    pkg_apt['bridge-utils'] = {
        'installed': True,
    }
    svc_systemd['networking'] = {
        'triggered': True,
        'cascade_skip': False,
        'needs': ['pkg_apt:bridge-utils'],
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
            'nameservers': node.metadata.get('networking', {}).get('nameservers', set()),
        },
    }
