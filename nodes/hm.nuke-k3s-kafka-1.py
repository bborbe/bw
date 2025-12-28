nodes['hm.nuke-k3s-kafka-1'] = {
    'hostname': 'nuke-k3s-kafka-1.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'optional': True,
                    'match': {
                        'name': 'en*',
                    },
                    'set-name': 'eth0',
                    'addresses': ['192.168.178.42/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.178.1',
                        }
                    ],
                    'nameservers': {
                        'addresses': ['8.8.8.8', '8.8.4.4'],
                        'search': ['hm.benjamin-borbe.de'],
                    },
                },
            },
        },
        'kvm-guest': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'k3s': {
            'enabled': True,
            'agent': True,
            'network': '192.168.178.0/24',
            'config': {
                'kubelet-arg': [
                    'image-gc-high-threshold=80',
                    'image-gc-low-threshold=70',
                    'eviction-hard=imagefs.available<10%',
                ]
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
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['sudo'],
            },
            'install': {
                'enabled': False,
            },
        },
    },
}
