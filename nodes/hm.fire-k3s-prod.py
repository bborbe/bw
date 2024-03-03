nodes['hm.fire-k3s-prod'] = {
    'hostname': 'fire-k3s-prod.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'k3s': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
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
