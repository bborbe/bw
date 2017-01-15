nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'bundles': (
        'ubuntu-desktop',
    ),
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'groups': {
            'data': {
                'enabled': True,
            },
        },
        'grub': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': [
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                ],
            },
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
        'kvm': {
            'enabled': True,
            'gui': True,
        },
        'networking': {
            'enabled': True,
            'nameservers': ['8.8.4.4', '8.8.8.8'],
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
            },
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
            },
            'jana': {
                'enabled': True,
            },
        },
        'smart': {
            'enabled': True,
        },
        'zfs': {
            'enabled': True,
            'pools': {
                'tank1': {
                    'type': 'raidz',
                    'devices': ['/dev/sdd', '/dev/sde', '/dev/sdf'],
                    'mounts': {
                        '/storage': {},
                        '/backup': {},
                        '/backup/fire.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
