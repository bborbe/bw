nodes['hm.nuke-k3s-longhorn-3'] = {
    'hostname': 'nuke-k3s-longhorn-3.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'kvm-guest': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'k3s': {
            'enabled': True,
            'agent': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    '-A INPUT -j ACCEPT',
                    '-A FORWARD -j ACCEPT',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['sudo'],
            },
            'install': {
                'enabled': False,
            },
        },
    },
}
