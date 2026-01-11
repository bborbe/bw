nodes['hm.sun'] = {
    'hostname': 'sun.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'samba': {
            'enabled': True,
            'server_name': 'sun.hm.benjamin-borbe.de',
        },
        'google-chrome': {
            'enabled': True,
        },
        'enpass': {
            'enabled': True,
        },
        'docker': {
            'enabled': True,
        },
        'gcloud-sdk': {
            'enabled': True,
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'kvm-host': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'enp9s0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'wakeonlan': False,
                },
                'enp10s0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'wakeonlan': False,
                },
            },
            'bridges': {
                'br0': {
                    'parameters': {
                        'stp': 'true',
                        'forward-delay': '4',
                    },
                    'mtu': 1500,
                    'macaddress': 'bc:5f:f4:71:15:c5',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['enp9s0'],
                    'addresses': ['192.168.30.2/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.30.1',
                        }
                    ],
                    'nameservers': {
                        'addresses': ['8.8.8.8', '8.8.4.4'],
                        'search': ['hm.benjamin-borbe.de'],
                    },
                },
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': set({
                    # '-A INPUT -j ACCEPT',
                    # '-A FORWARD -j ACCEPT',
                }),
            },
        },
        'smart': {
            'enabled': True,
        },
        'grub': {
            'predictable-nic': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo', 'libvirt', 'docker'],
            },
            'data': {
                'enabled': True,
                'groups': [],
                'ssun': '/usr/sbin/nologin',
            },
        },
        'groups': {
            'data': {
                'enabled': True,
            },
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
    },
}
