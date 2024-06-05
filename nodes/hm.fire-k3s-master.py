nodes['hm.fire-k3s-master'] = {
    'hostname': 'fire-k3s-master.hm.benjamin-borbe.de',
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
