nodes['hm.nuke-k3s-master-2'] = {
    'hostname': 'nuke-k3s-master-2.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
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
                    'addresses': ['192.168.178.40/24'],
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
            'config': {
                'disable': 'local-storage',
                'kube-controller-manager-arg': [
                    'node-cidr-mask-size=22'
                ],
                'kubelet-arg': [
                    'image-gc-high-threshold=90',
                    'image-gc-low-threshold=80',
                ]
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    '-A INPUT -j ACCEPT',
                    '-A FORWARD -j ACCEPT',
                },
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
