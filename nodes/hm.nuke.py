nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'ubuntu-desktop': {
            'enabled': True,
        },
        'kvm': {
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
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
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
                    'macaddress': '70:85:c2:b9:64:65',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['eth0'],
                    'addresses': ['192.168.178.5/24'],
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
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo', 'libvirt'],
            },
        },
    },
}
