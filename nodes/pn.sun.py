nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'dns-update': {
            'enabled': True,
            'updates': {
                'pn.benjamin-borbe.de': {
                    'zone': 'benjamin-borbe.de',
                    'node': 'pn',
                    'dns-server': 'ns.rocketsource.de',
                    'ip-url': 'https://ip.benjamin-borbe.de',
                    'private': teamvault.file('aL50O8', site='benjamin-borbe'),
                    'key': teamvault.file('9L64w3', site='benjamin-borbe'),
                },
            },
        },
        'git': {
            'clones': {
                'kubernetes': {
                    'repo': 'https://github.com/bborbe/kubernetes-cluster-sun.git',
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
            'nat_interfaces': ['br0'],
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
        },
        'networking': {
            'enabled': True,
            'nameservers': ['8.8.4.4', '8.8.8.8'],
            'interfaces': {
                'eth0': {},
                'br0': {
                    'address': '192.168.2.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.2.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'host-k8s': {
                    'address': '172.16.72.1',
                    'netmask': '255.255.255.0',
                    'pre-up': 'brctl addbr host-k8s',
                    'post-down': 'brctl delbr host-k8s',
                },
            },
        },
        'openvpn': {
            'enabled': True,
        },
        'nfs-server': {
            'enabled': True,
            'exports': {
                '/backup/fire.hm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/host.sm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/kubernetes-backup.sm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/nova.hm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/nuke.hm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/v22016124049440903.goodsrv.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/rasp.hm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/star.hm.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
                '/backup/sun.pn.benjamin-borbe.de': {
                    '172.16.72.0/24': ['rw', 'async', 'no_subtree_check', 'no_root_squash'],
                },
            },
        },
        'samba': {
            'enabled': True,
            'server_name': 'sun.pn.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'timemachine': {
            'enabled': True,
            'users': {
                'borbe': {
                    'path': '/timemachine/borbe.pn.benjamin-borbe.de',
                    'password': teamvault.password('mwxBLK', site='benjamin-borbe'),
                    'size': '400000',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'libvirtd'],
            },
            'walter': {
                'enabled': True,
                'groups': ['data'],
            },
            'brigitte': {
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
                        '/backup': {},
                        '/backup/fire.hm.benjamin-borbe.de': {},
                        '/backup/host.sm.benjamin-borbe.de': {},
                        '/backup/kubernetes-backup.sm.benjamin-borbe.de': {},
                        '/backup/nova.hm.benjamin-borbe.de': {},
                        '/backup/nuke.hm.benjamin-borbe.de': {},
                        '/backup/v22016124049440903.goodsrv.de': {},
                        '/backup/rasp.hm.benjamin-borbe.de': {},
                        '/backup/star.hm.benjamin-borbe.de': {},
                        '/backup/sun.pn.benjamin-borbe.de': {},
                        '/data': {},
                        '/timemachine': {},
                        '/timemachine/borbe.pn.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
