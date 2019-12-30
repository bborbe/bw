nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'bionic',
        'backup_server': {
            'enabled': True,
            'targets': {
                'sun.pn.benjamin-borbe.de': {'allow': '192.168.178.3/32'},
            }
        },
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
                'filter': {
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
                },
            },
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
                'up route add -net 172.16.24.0/24 gw 192.168.178.5': {},
                'up route add -net 192.168.2.0/24 gw 192.168.178.2': {},
            },
        },
        'samba': {
            'enabled': True,
            'server_name': 'fire.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'timemachine': {
            'enabled': True,
            'users': {
                'nova': {
                    'path': '/timemachine/nova.hm.benjamin-borbe.de',
                    'password_hash': 'BwjGOV',
                    'size': '600000',
                },
                'star': {
                    'path': '/timemachine/star.hm.benjamin-borbe.de',
                    'password_hash': 'BOrkLo',
                    'size': '400000',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'libvirtd', 'sudo'],
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
                    'devices': ['/dev/sdc', '/dev/sdd', '/dev/sde'],
                    'mounts': {
                        '/backup': {},
                        '/data': {},
                        '/home': {},
                        '/home/bborbe': {},
                        '/home/jana': {},
                        '/timemachine': {},
                        '/timemachine/nova.hm.benjamin-borbe.de': {},
                        '/timemachine/star.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
