os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'iptables': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
    'iptables-persistent': {
        'installed': False,
    },
    'netfilter-persistent': {
        'installed': False,
    },
}

files = {}

files['/etc/network/if-pre-up.d/iptables'] = {
    'delete': True,
}

if node.metadata.get('iptables', {}).get('enabled', False):
    files['/etc/network/if-pre-up.d/10-iptables-flush'] = {
        'source': '10-iptables-flush',
        'content_type': 'mako',
        'mode': '0775',
        'owner': 'root',
        'group': 'root',
        'context': {},
    }
else:
    files['/etc/network/if-pre-up.d/10-iptables-flush'] = {
        'delete': True,
    }

if node.metadata.get('iptables', {}).get('enabled', False):
    files['/etc/network/if-pre-up.d/20-iptables-rules'] = {
        'source': '20-iptables-rules',
        'content_type': 'mako',
        'mode': '0775',
        'owner': 'root',
        'group': 'root',
        'context': {
            'rules': node.metadata.get('iptables', {}).get('rules', []),
            'nat_interfaces': node.metadata.get('iptables', {}).get('nat_interfaces', []),
        },
        'triggers': ['action:iptables-insert'],
    }
else:
    files['/etc/network/if-pre-up.d/20-iptables-rules'] = {
        'delete': True,
    }

actions = {
    'iptables-insert': {
        'command': '/etc/network/if-pre-up.d/20-iptables-rules',
        'needs': ['pkg_apt:iptables'],
        'triggered': True,
    },
}
