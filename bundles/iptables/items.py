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
        'needs': ['pkg_apt:iptables', 'pkg_apt:iptables-persistent'],
        'triggered': True,
    },
    'iptables-restore-ipv6': {
        'command': 'ip6tables-restore < /etc/iptables/rules.v6',
        'needs': ['pkg_apt:iptables', 'pkg_apt:iptables-persistent'],
        'triggered': True,
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
            'rules': node.metadata.get('iptables', {}).get('rules', []),
            'nat_interfaces': node.metadata.get('iptables', {}).get('nat_interfaces', []),
        },
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
        'context': {},
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
