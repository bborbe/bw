nodes['hm.nuke-k3s-prod-master-0'] = {
    'hostname': 'nuke-k3s-prod-master-0.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'openvpn-client': {
            'enabled': True,
            'name': 'nuke-k3s-prod-master-0',
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
                    'addresses': ['192.168.178.37/24'],
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
                # max-pods=512 alone is not enough: k3s defaults each node to a /24
                # podCIDR (254 usable IPs), so kubelet advertises 512 while flannel
                # can only hand out 254. Hit on 2026-08-19 -- 41 pods stuck in
                # ContainerCreating with "no IP addresses available in range set:
                # 10.42.1.1-10.42.1.254" on nuke-k3s-dev-worker-0 at 299 pods.
                # quant's masters have carried this since its own big nodes were
                # re-joined; it was missed when the nuke node files were written.
                'kube-controller-manager-arg': [
                    'node-cidr-mask-size=22'
                ],
                'kubelet-arg': [
                    'image-gc-high-threshold=80',
                    'image-gc-low-threshold=70',
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
