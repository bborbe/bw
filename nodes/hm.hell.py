nodes['hm.hell'] = {
    'hostname': 'hell.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'groups': {
            'data': {
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
                    'address': '192.168.178.9',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
        'samba': {
            'enabled': True,
            'server_name': 'hell.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo'],
            },
            'jana': {
                'enabled': True,
                'groups': ['data'],
            },
        },
        'zfs': {
            'enabled': True,
            'pools': {
                'tank1': {
                    'type': 'raidz',
                    'devices': ['/dev/sdb', '/dev/sdc', '/dev/sdd'],
                    'mounts': {
                        '/data': {},
                    },
                },
                'tank2': {
                    'type': 'raidz',
                    'devices': ['/dev/sde', '/dev/sdf', '/dev/sdg'],
                    'mounts': {
                        '/backup': {},
                    },
                },
            },
        },
    },
}
