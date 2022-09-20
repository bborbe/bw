nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'groups': {
        'ubuntu-bionic',
    },
    'metadata': {
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.16.4',
            'os': 'linux',
        },
        'backup_server': {
            'enabled': True,
            'targets': {
                'co2hz.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'co2wz.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'fire.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'nova.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'nuke.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'rasp3.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'rasp4.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'star.hm.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'sun.pn.benjamin-borbe.de': {'allow': '192.168.2.3/32'},
                'v22016124049440903.goodsrv.de': {'allow': '192.168.2.3/32'},
            }
        },
        'groups': {
            'data': {
                'enabled': True,
            },
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
                    'address': '192.168.2.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.2.1',
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
