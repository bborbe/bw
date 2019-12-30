nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'bionic',
        'backup_server': {
            'enabled': True,
            'targets': {
                'co2hz.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'co2wz.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'fire.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'nova.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'nuke.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'rasp.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'star.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'sun.pn.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'v22016124049440903.goodsrv.de': {'allow': '192.168.2.3/32'},
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
                    'private_hash': 'aL50O8',
                    'key_hash': '9L64w3',
                },
            },
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
                    'address': '192.168.2.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.2.1',
                },
            },
        },
        'openvpn': {
            'enabled': True,
            'services': {
                'home.benjamin-borbe.de': {
                    'enabled': True,
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
                    'password_hash': 'mwxBLK',
                    'size': '400000',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data'],
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
