if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

files = {}
directories = {}
svc_systemd = {}
pkg_apt = {}

if node.metadata.get('netplan', {}).get('enabled', False):
    pkg_apt['resolvconf'] = {
        'installed': False,
    }
    pkg_apt['network-manager'] = {
        'installed': False,
    }
    pkg_apt['bridge-utils'] = {
        'installed': True,
    }
    actions = {
        'netplan_apply': {
            'command': 'netplan apply',
            'triggered': True,
        },
    }
    directories['/etc/netplan'] = {
        'mode': '0755',
        'owner': 'root',
        'group': 'root',
        'purge': True,
    }
    files['/etc/netplan/static.yaml'] = {
        'source': 'netplan-static',
        'owner': 'root',
        'group': 'root',
        'mode': '0600',
        'content_type': 'mako',
        'context': {
            'ethernets': node.metadata.get('netplan', {}).get('ethernets', {}),
            'bridges': node.metadata.get('netplan', {}).get('bridges', {}),
        },
        'triggers': ['action:netplan_apply'],
    }
