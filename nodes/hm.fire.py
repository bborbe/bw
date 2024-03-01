nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.21.7',
            'os': 'linux',
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'k3s': {
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
        },
        'docker-registry': {
            'enabled': True,
        },
        'kvm': {
            'enabled': True,
        },
        # 'backup_server': {
        #     'enabled': True,
        #     'targets': {
        #         'sun.pn.benjamin-borbe.de': {'allow': '192.168.178.3/32'},
        #     }
        # },
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
                    'macaddress': 'd0:50:99:5a:18:be',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['eth0'],
                    'addresses': ['192.168.178.3/24'],
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
            'server_name': 'fire.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo', 'libvirt'],
            },
            'jana': {
                'enabled': True,
                'groups': ['data'],
            },
            'data': {
                'enabled': True,
                'groups': [],
                'shell': '/usr/sbin/nologin',
            },
            'k8s': {
                'enabled': True,
                'groups': [],
                'shell': '/usr/sbin/nologin',
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
                        '/var/lib/rancher/k3s/storage/hdd': {},
                    },
                },
            },
        },
    },
}
