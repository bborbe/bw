nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-bionic',
    },
    'metadata': {
        'backup_server': {
            'enabled': True,
            'targets': {
                'fire.hm.benjamin-borbe.de': {'allow': '192.168.178.5/32'},
            }
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.15.6',
            'os': 'linux',
        },
        'groups': {
            'data': {
                'enabled': True,
            },
        },
        'grub': {
            'default': 'Windows Boot Manager (on /dev/nvme0n1p2)',
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
                'groups': ['libvirtd', 'sudo'],
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
                        '/backup': {},
                        '/home': {},
                        '/home/bborbe': {},
                        '/home/jana': {},
                    },
                },
            },
        },
    },
}
