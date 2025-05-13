nodes['hm.nuke'] = {
    'hostname': 'nuke.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'systemd': {
            'disable-power-button': True,
        },
        'backup_client': {
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
        'docker': {
            'enabled': True,
        },
        'gcloud-sdk': {
            'enabled': True,
        },
        'grub': {
            'predictable-nic': True,
        },
        'udev': {
            'eth0': 'a8:a1:59:7e:f8:22',
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
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.24.3',
            'os': 'linux',
        },
        'smart': {
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
                    'macaddress': '70:85:c2:b9:64:66',
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
