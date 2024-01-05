nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'docker': {
            'enabled': True,
        },
        'groups': {
            'data': {
                'enabled': True,
            },
            'docker': {
                'enabled': True,
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
                },
            },
        },
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['docker', 'data', 'sudo'],
            },
        },
    },
}
