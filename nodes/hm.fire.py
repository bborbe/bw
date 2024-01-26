nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'k3s': {
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
        },
        'docker-registry': {
            'enabled': True,
        },
        # 'docker': {
        #     'enabled': True,
        # },
        'backup_server': {
            'enabled': True,
            'targets': {
                'sun.pn.benjamin-borbe.de': {'allow': '192.168.178.3/32'},
            }
        },
        # 'golang': {
        #     'enabled': True,
        #     'arch': 'amd64',
        #     'version': '1.16.4',
        #     'os': 'linux',
        # },
        'groups': {
            'data': {
                'enabled': True,
            },
            # 'docker': {
            #     'enabled': True,
            # },
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
                    'address': '192.168.178.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
        'samba': {
            'enabled': True,
            'server_name': 'fire.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo'],
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
                    'devices': ['/dev/sda', '/dev/sdb', '/dev/sdc'],
                    'mounts': {
                        '/backup': {},
                        '/data': {},
                        '/home': {},
                        '/home/bborbe': {},
                        '/home/jana': {},
                        '/var/lib/docker-registry': {},
                    },
                },
            },
        },
    },
}
