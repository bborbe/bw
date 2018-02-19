nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'backup_server': {
            'enabled': True,
            'targets': {
                'fire.hm.benjamin-borbe.de': {'allow': '172.16.24.0/24'},
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
                },
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
            'interfaces': {
                'eth0': {},
                'br0': {
                    'address': '192.168.178.5',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'host-k8s': {
                    'address': '172.16.24.1',
                    'netmask': '255.255.255.0',
                    'pre-up': 'brctl addbr host-k8s',
                    'post-down': 'brctl delbr host-k8s',
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
