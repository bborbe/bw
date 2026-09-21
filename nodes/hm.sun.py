nodes['hm.sun'] = {
    'hostname': 'sun.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'openvpn-client': {
            'enabled': True,
            'name': 'sun',
        },
        'workspace': {
            'enabled': True,
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
        # sun is the `make buca` build host: it builds FROM a pinned golang
        # image. Alert if that base layer disappears, so a prune surfaces as an
        # event rather than as a slow rebuild. The probe is version-agnostic on
        # purpose -- the pin moves (1.26.4 -> 1.27.1) and a pinned probe would
        # go blind on the next bump.
        # See: 65 Runbooks/Sun Disk Cleanup.md
        'monit': {
            'checks': {
                'docker-golang-base-layer': {
                    'template': 'docker-golang-base-layer.conf',
                    'script': 'docker-golang-base-layer',
                },
            },
        },
        'trivy': {
            'enabled': True,
        },
        'samba': {
            'enabled': True,
            'server_name': 'sun.hm.benjamin-borbe.de',
            'shares': {
                'data': {
                    'comment': 'Data',
                    'path': '/data',
                    'valid_users': '@data',
                    'force_group': 'data',
                },
            },
            'homes': {
                'enabled': True,
                'valid_users': ['bborbe', 'jana', 'brigitte', 'walter'],
            },
        },
        'google-chrome': {
            'enabled': True,
        },
        'enpass': {
            'enabled': True,
        },
        'gcloud-sdk': {
            'enabled': True,
        },
        'helm': {
            'enabled': True,
        },
        'ubuntu-desktop': {
            'enabled': True,
        },
        'kvm-host': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'enp9s0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'wakeonlan': False,
                },
                'enp10s0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'wakeonlan': False,
                    'optional': True,
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
                    'interfaces': ['enp9s0'],
                    'addresses': ['192.168.30.2/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.30.1',
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
                    '-A INPUT -m state --state NEW -p tcp --dport 8188 -j ACCEPT',
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
        'ssh': {
            'allow_agent_forwarding': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo', 'libvirt', 'docker', 'ollama'],
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
    },
}
