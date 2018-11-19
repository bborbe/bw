nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'bionic',
        'backup_server': {
            'enabled': True,
            'targets': {
                'fire.hm.benjamin-borbe.de': {'allow': '192.168.178.5/32'},
            }
        },
        'git': {
            'clones': {
                'kubernetes': {
                    'repo': 'https://github.com/bborbe/kubernetes-cluster-nuke.git',
                    'target': '/var/lib/libvirt/images/kubernetes',
                },
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
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
                'up route add -net 172.16.22.0/24 gw 192.168.178.3': {},
                'up route add -net 192.168.2.0/24 gw 192.168.178.2': {},
            },
        },
        'nfs-server': {
            'enabled': True,
        },
        'ubuntu-desktop': {
            'enabled': False,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['libvirtd'],
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
