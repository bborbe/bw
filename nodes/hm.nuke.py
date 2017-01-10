nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'bundles': (
        'ubuntu-desktop',
    ),
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'networking': {
            'enabled': True,
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'dns-nameservers': '8.8.4.4 8.8.8.8',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
            },
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
        'grub': {
            'enabled': True,
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
        'ubuntu-desktop': {
            'enabled': True,
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
                        '/backup/freenas.hm.benjamin-borbe.de': {},
                        '/backup/fire.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
