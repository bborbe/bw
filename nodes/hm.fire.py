import bwtv as teamvault

nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
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
                'eth0': {},
                'br0': {
                    'address': '192.168.178.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'host-k8s': {
                    'address': '172.16.22.1',
                    'netmask': '255.255.255.0',
                    'pre-up': 'brctl addbr host-k8s',
                    'post-down': 'brctl delbr host-k8s',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
                # 'up route add -net 172.16.72.0/24 gw 192.168.178.2': {},
                # 'up route add -net 172.16.80.0/24 gw 192.168.178.2': {},
                'up route add -net 192.168.2.0/24 gw 192.168.178.2': {},
            },
        },
        'nfs-server': {
            'enabled': True,
            'exports': {
                '/backup/sun.pn.benjamin-borbe.de': {
                    '172.16.22.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
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
                'groups': ['data', 'libvirtd'],
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
                        '/backup/sun.pn.benjamin-borbe.de': {},
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
