nodes['hm.nuke-k3s-master-0'] = {
    'hostname': 'nuke-k3s-master-0.hm.benjamin-borbe.de',
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
                    'addresses': ['192.168.178.38/24'],
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
            'network': '192.168.178.0/24',
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
                'filter': set({
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 30000:32767 -j ACCEPT',
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
