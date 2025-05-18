nodes['hm.sun'] = {
    'hostname': 'sun.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'docker': {
            'enabled': True,
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'kvm-host': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'enp10s0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'wakeonlan': True,
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
                    'interfaces': ['enp10s0'],
                    'addresses': ['192.168.177.9/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.177.1',
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
            'version': '1.24.3',
            'os': 'linux',
        },
    },
}
