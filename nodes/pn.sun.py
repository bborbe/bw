import bwtv as teamvault

nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'backup_server': {
            'enabled': True,
            'targets': {
                'co2hz.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'co2wz.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'fire.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'nova.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'nuke.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'rasp.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'star.hm.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'sun.pn.benjamin-borbe.de': {'allow': '172.16.72.0/24'},
                'v22016124049440903.goodsrv.de': {'allow': '172.16.72.0/24'},
            }
        },
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
        },
        'networking': {
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
                        '/data': {},
                        '/timemachine': {},
                        '/timemachine/borbe.pn.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
