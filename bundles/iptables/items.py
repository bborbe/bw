os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'iptables': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
    'iptables-persistent': {
        'installed': node.metadata.get('iptables', {}).get('enabled', False),
    },
}

if node.metadata.get('iptables', {}).get('enabled', False):
    files = {
        '/etc/network/if-pre-up.d/iptables': {
            'source': 'iptables',
            'content_type': 'mako',
            'mode': '0775',
            'owner': 'root',
            'group': 'root',
            'context': {
                'rules': node.metadata.get('iptables', {}).get('rules', []),
            },
            'triggers': ['action:iptables-insert'],
        },
    }

actions = {
    'iptables-insert': {
        'command': '/etc/network/if-pre-up.d/iptables',
        'needs': ['pkg_apt:iptables'],
        'triggered': True,
    },
}
