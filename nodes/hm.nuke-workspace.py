nodes['hm.nuke-workspace'] = {
    'hostname': 'nuke-workspace.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'apt': {
            'packages': {
                'gnupg2': {'installed': True},
                'pinentry-tty': {'installed': True},
                'build-essential': {'installed': True},
                'libssl-dev': {'installed': True},
                'zlib1g-dev': {'installed': True},
                'libbz2-dev': {'installed': True},
                'libreadline-dev': {'installed': True},
                'libsqlite3-dev': {'installed': True},
                'wget': {'installed': True},
                'curl': {'installed': True},
                'llvm': {'installed': True},
                'xz-utils': {'installed': True},
                'tk-dev': {'installed': True},
                'libxml2-dev': {'installed': True},
                'libxmlsec1-dev': {'installed': True},
                'libffi-dev': {'installed': True},
                'liblzma-dev': {'installed': True},
                'git': {'installed': True},
                'keychain': {'installed': True},
                'direnv': {'installed': True},
            },
        },
        'kubectl': {
            'enabled': True,
            'version': 'v1.35',
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'docker': {
            'enabled': True,
        },
        'trivy': {
            'enabled': True,
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
                    'addresses': ['192.168.178.29/24'],
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
                'groups': ['sudo', 'docker'],
            },
            'install': {
                'enabled': False,
            },
        },
    },
}
