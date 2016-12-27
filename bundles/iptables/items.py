os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'iptables': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
    'iptables-persistent': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
    'netfilter-persistent': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
}

files = {}

actions = {
    'iptables-restore-ipv4': {
        'command': 'iptables-restore < /etc/iptables/rules.v4',
        'triggered': True,
        'cascade_skip': False,
    },
    'iptables-restore-ipv6': {
        'command': 'ip6tables-restore < /etc/iptables/rules.v6',
        'triggered': True,
        'cascade_skip': False,
    },
}

if node.metadata.get('iptables', {}).get('enabled', False):
    files['/etc/iptables/rules.v4'] = {
        'source': 'rules.v4',
        'content_type': 'mako',
        'mode': '0775',
        'owner': 'root',
        'group': 'root',
        'context': {
            'nat_interfaces': node.metadata.get('iptables', {}).get('nat_interfaces', []),
            'mangle': node.metadata.get('iptables', {}).get('rules', {}).get('mangle', []),
            'nat': node.metadata.get('iptables', {}).get('rules', {}).get('nat', []),
            'filter': node.metadata.get('iptables', {}).get('rules', {}).get('filter', []),
        },
        'needs': ['pkg_apt:iptables', 'pkg_apt:iptables-persistent'],
        'triggers': ['action:iptables-restore-ipv4'],
    }
else:
    files['/etc/iptables/rules.v4'] = {
        'delete': True,
    }

if node.metadata.get('iptables', {}).get('enabled', False):
    files['/etc/iptables/rules.v6'] = {
        'source': 'rules.v6',
        'content_type': 'mako',
        'mode': '0775',
        'owner': 'root',
        'group': 'root',
        'context': {
            'mangle': node.metadata.get('iptables', {}).get('rules', {}).get('mangle_v6', []),
            'nat': node.metadata.get('iptables', {}).get('rules', {}).get('nat_v6', []),
            'filter': node.metadata.get('iptables', {}).get('rules', {}).get('filter_v6', []),
        },
        'needs': ['pkg_apt:iptables', 'pkg_apt:iptables-persistent'],
        'triggers': ['action:iptables-restore-ipv6'],
    }
else:
    files['/etc/iptables/rules.v6'] = {
        'delete': True,
    }

files['/etc/network/if-pre-up.d/iptables'] = {
    'delete': True,
}

files['/etc/network/if-pre-up.d/10-iptables-flush'] = {
    'delete': True,
}

files['/etc/network/if-pre-up.d/20-iptables-rules'] = {
    'delete': True,
}
