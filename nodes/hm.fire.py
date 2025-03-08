nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'systemd': {
            'disable-power-button': True,
        },
        'docker': {
            'enabled': True,
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'enpass': {
            'enabled': True,
        },
        'intellij': {
            'enabled': True,
        },
        'google-chrome': {
            'enabled': True,
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.24.1',
            'os': 'linux',
        },
        'backup_client': {
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
        },
        'docker-registry': {
            'enabled': True,
        },
        'kvm-host': {
            'enabled': True,
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
                'groups': ['data', 'sudo', 'libvirt', 'docker'],
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
