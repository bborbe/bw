import bwtv as teamvault

nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
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
                    'pre-down': '/sbin/ethtool -s eth0 wol g',
                },
                'br0': {
                    'address': '192.168.178.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'br0:0': {
                    'address': '172.16.23.3',
                    'netmask': '255.255.255.0',
                },
                'host-k8s': {
                    'address': '172.16.22.1',
                    'netmask': '255.255.255.0',
                    'pre-up': 'brctl addbr host-k8s',
                    'post-down': 'brctl delbr host-k8s',
                },
            },
            'routes': {
                'up route add -net 172.16.30.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.40.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.50.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.70.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.71.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.72.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.80.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.90.0/24 gw 172.16.23.2': {},
            },
        },
        'nfs-server': {
            'enabled': True,
            'exports': {
                '/backup/sun.pn.benjamin-borbe.de': {
                    '172.16.22.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash', 'fsid=0'],
                },
                '/backup/freenas.pn.benjamin-borbe.de': {
                    '172.16.22.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash', 'fsid=0'],
                },
                '/backup/pfsense.pn.benjamin-borbe.de': {
                    '172.16.22.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash', 'fsid=0'],
                },
            },
        },
        'samba': {
            'enabled': True,
        },
        'smart': {
            'enabled': True,
        },
        'timemachine': {
            'enabled': True,
            'users': {
                'nova': {
                    'path': '/timemachine/nova.hm.benjamin-borbe.de',
                    'password': teamvault.password('BwjGOV', site='benjamin-borbe'),
                    'size': '400000',
                },
                'star': {
                    'path': '/timemachine/star.hm.benjamin-borbe.de',
                    'password': teamvault.password('BOrkLo', site='benjamin-borbe'),
                    'size': '400000',
                },
            },
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data'],
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
                        '/data': {},
                        '/home/jana': {},
                        '/home/bborbe': {},
                        '/backup/sun.pn.benjamin-borbe.de': {},
                        '/backup/freenas.pn.benjamin-borbe.de': {},
                        '/backup/pfsense.pn.benjamin-borbe.de': {},
                        '/timemachine/star.hm.benjamin-borbe.de': {},
                        '/timemachine/nova.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
