nodes['hm.hell'] = {
    'hostname': 'hell.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
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
                },
            },
        },
        'k3s': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                },
            },
            'bridges': {
                'br0': {
                    'parameters': {
                        'stp': 'true',
                        'forward-delay': '4',
                    },
                    'mtu': 1500,
                    'macaddress': 'bc:5f:f4:71:15:c4',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['eth0'],
                    'addresses': ['192.168.178.9/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.178.1',
                        }
                    ],
                    'nameservers': ['8.8.8.8', '8.8.4.4'],
                },
            },
        },
        'samba': {
            'enabled': True,
            'server_name': 'hell.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo'],
            },
            'data': {
                'enabled': True,
                'groups': [],
                'shell': '/usr/sbin/nologin',
            },
        },
        'backup_server': {
            'enabled': True,
            'pool': 'tank2',
            'targets': {
                'co2hz.hm.benjamin-borbe.de': {},
                'co2wz.hm.benjamin-borbe.de': {},
                'fire-k3s-dev.hm.benjamin-borbe.de': {},
                'fire-k3s-master.hm.benjamin-borbe.de': {},
                'fire-k3s-prod.hm.benjamin-borbe.de': {},
                'fire.hm.benjamin-borbe.de': {},
                'hetzner-1.benjamin-borbe.de': {},
                'nuke.hm.benjamin-borbe.de': {},
                'rasp3.hm.benjamin-borbe.de': {},
                'rasp4.hm.benjamin-borbe.de': {},
            }
        },
        'zfs': {
            'enabled': True,
            'pools': {
                'tank1': {
                    'type': 'raidz',
                    'devices': ['/dev/sdb', '/dev/sdc', '/dev/sdd'],
                    'mounts': {
                        '/data': {},
                    },
                },
                'tank2': {
                    'type': 'raidz',
                    'devices': ['/dev/sde', '/dev/sdf', '/dev/sdg'],
                    'mounts': {
                        '/backup': {},
                        # '/backup/fire.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
