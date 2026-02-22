nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'systemd': {
            'disable-power-button': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'docker': {
            'enabled': True,
        },
        'gcloud-sdk': {
            'enabled': True,
        },
        'grub': {
            'predictable-nic': True,
        },
        'mdadm': {
            '/dev/md0': {
                'level': 'raid5',
                'num-devices': '4',
                'metadata': '1.2',
                'name': 'nuke:0',
                'uuid': '625d2f94:60c6852c:40cc4d28:f0733ac8',
                'devices': ['/dev/nvme0n1', '/dev/nvme1n1', '/dev/nvme2n1', '/dev/nvme3n1'],
            }
        },
        'msmtp': {
            'enabled': True,
            'host': '172.16.90.1',
            'port': 25,
            'from': 'root@nuke.hm.benjamin-borbe.de',
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'smart': {
            'enabled': True,
        },
        'kvm-host': {
            'enabled': True,
            'nwfilters': {
                'nuke-boss': {
                    'rules': [
                        {'action': 'accept', 'ip': '192.168.178.1'},  # opnsense (internet/trading API)
                        {'action': 'accept', 'ip': '192.168.178.38', 'port': 443},  # k8s master-0 (HTTPS ingresses)
                        {'action': 'accept', 'ip': '192.168.178.39', 'port': 443},  # k8s master-1 (HTTPS ingresses)
                        {'action': 'accept', 'ip': '192.168.178.40', 'port': 443},  # k8s master-2 (HTTPS ingresses)
                        {'action': 'drop', 'subnet': '192.168.178.0/24'},  # block direct K8s access
                        {'action': 'accept', 'all': True},  # allow everything else (internet, SSH)
                    ],
                },
                'nuke-workspace': {
                    'rules': [
                        {'action': 'accept', 'ip': '192.168.178.1'},  # opnsense (internet/trading API)
                        {'action': 'accept', 'ip': '192.168.178.38', 'port': 6443},  # k8s master-0 (kubectl)
                        {'action': 'accept', 'ip': '192.168.178.39', 'port': 6443},  # k8s master-1 (kubectl)
                        {'action': 'accept', 'ip': '192.168.178.40', 'port': 6443},  # k8s master-2 (kubectl)
                        {'action': 'accept', 'ip': '192.168.178.38', 'port': 443},  # k8s master-0 (HTTPS ingresses)
                        {'action': 'accept', 'ip': '192.168.178.39', 'port': 443},  # k8s master-1 (HTTPS ingresses)
                        {'action': 'accept', 'ip': '192.168.178.40', 'port': 443},  # k8s master-2 (HTTPS ingresses)
                        {'action': 'drop', 'subnet': '192.168.178.0/24'},  # block other K8s nodes
                        {'action': 'accept', 'all': True},  # allow everything else (internet, SSH)
                    ],
                },
            },
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
                'enp6s0': {
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
                    'macaddress': '70:85:c2:b9:64:66',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['enp6s0'],
                    'addresses': ['192.168.178.5/24'],
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
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo', 'libvirt', 'docker'],
            },
        },
    },
}
