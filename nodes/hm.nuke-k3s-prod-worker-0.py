nodes['hm.nuke-k3s-prod-worker-0'] = {
    'hostname': 'nuke-k3s-prod-worker-0.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'openvpn-client': {
            'enabled': True,
            'name': 'nuke-k3s-prod-worker-0',
        },
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
                    'addresses': ['192.168.178.44/24'],
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
                    # GC starts at 70% used = 30% free, not 80% used = 20% free.
                    # DiskRootOutOfSpace fires below 20% free, so at high=80 the node was
                    # designed to sit exactly on the alert line and undershot it at every
                    # trough. Measured 2026-10-23: 144 space-triggered image GCs and 2,568
                    # image pulls in 24h, free space oscillating 10.5%-42.2%.
                    'image-gc-high-threshold=70',
                    'image-gc-low-threshold=60',
                    'eviction-hard=imagefs.available<10%',
                    'max-pods=512',
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
