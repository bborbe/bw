import bwtv as teamvault

nodes['hz.hetzner-2'] = {
    'hostname': 'hetzner-2.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': True,
                    'dhcp6': False,
                },
            },
        },
        'workspace': {
            'enabled': True,
        },
        'openclaw': {
            'enabled': True,
            'matrix': {
                'enabled': True,
                'homeserver': 'https://matrix.benjamin-borbe.de',
                'user_id': teamvault.username('7qGn5L', site='benjamin-borbe'),
                'password': teamvault.password('7qGn5L', site='benjamin-borbe'),
            },
        },
        'hermes': {
            'enabled': True,
            'matrix': {
                'enabled': True,
                'homeserver': 'https://matrix.benjamin-borbe.de',
                'user_id': teamvault.username('VO053L', site='benjamin-borbe'),
                'password': teamvault.password('VO053L', site='benjamin-borbe'),
            },
            'brave': {
                'enabled': True,
                'api_key': teamvault.password('dwkkzw', site='benjamin-borbe'),
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    # '-A FORWARD -j ACCEPT',
                    # '-A FORWARD -i tun0 -o tun0 -j DROP',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
            },
        },
        'kubectl': {
            'enabled': True,
            'version': 'v1.35',
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'trivy': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
    },
}
