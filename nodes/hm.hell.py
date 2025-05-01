nodes['hm.hell'] = {
    'hostname': 'hell.hm.benjamin-borbe.de',
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
                    'wakeonlan': True,
                },
            },
            'bridges': {
                'br0': {
                    'parameters': {
                        'stp': 'true',
                        'forward-delay': '4',
                    },
                    'mtu': 1500,
                    'macaddress': 'bc:5f:f4:71:15:c4',
                    'dhcp4': False,
                    'dhcp6': False,
                    'interfaces': ['eth0'],
                    'addresses': ['192.168.180.9/24'],
                    'routes': [
                        {
                            'to': 'default',
                            'via': '192.168.180.1',
                        }
                    ],
                    'nameservers': {
                        'addresses': ['192.168.180.1'],
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
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 30000:32767 -j ACCEPT',
                    # '-A INPUT -j ACCEPT',
                    # '-A FORWARD -j ACCEPT',
                }),
            },
        },
        'k3s': {
            'enabled': True,
            'network': '192.168.180.9/32',
        },
        'samba': {
            'enabled': True,
            'server_name': 'hell.hm.benjamin-borbe.de',
        },
        'smart': {
            'enabled': True,
        },
        'users': {
            'bborbe': {
                'enabled': True,
                'groups': ['data', 'sudo'],
            },
            'data': {
                'enabled': True,
                'groups': [],
                'shell': '/usr/sbin/nologin',
            },
        },
        'groups': {
            'data': {
                'enabled': True,
            },
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.24.2',
            'os': 'linux',
        },
        'backup_server': {
            'enabled': True,
            'pool': 'tank2',
            'targets': {
                'burn.hm.benjamin-borbe.de': {},
                'co2hz.hm.benjamin-borbe.de': {},
                'co2wz.hm.benjamin-borbe.de': {},
                'fire.hm.benjamin-borbe.de': {},
                'hetzner-1.benjamin-borbe.de': {},
                'nuke-k3s-agent-0.hm.benjamin-borbe.de': {},
                'nuke-k3s-agent-1.hm.benjamin-borbe.de': {},
                'nuke-k3s-agent.hm.benjamin-borbe.de': {},
                'nuke-k3s-dev-0.hm.benjamin-borbe.de': {},
                'nuke-k3s-kafka-0.hm.benjamin-borbe.de': {},
                'nuke-k3s-kafka-1.hm.benjamin-borbe.de': {},
                'nuke-k3s-kafka-2.hm.benjamin-borbe.de': {},
                'nuke-k3s-longhorn-0.hm.benjamin-borbe.de': {},
                'nuke-k3s-longhorn-1.hm.benjamin-borbe.de': {},
                'nuke-k3s-master-0.hm.benjamin-borbe.de': {},
                'nuke-k3s-master-1.hm.benjamin-borbe.de': {},
                'nuke-k3s-master-2.hm.benjamin-borbe.de': {},
                'nuke-k3s-prod-0.hm.benjamin-borbe.de': {},
                'nuke.hm.benjamin-borbe.de': {},
                'rasp3.hm.benjamin-borbe.de': {},
            }
        },
        'zfs': {
            'enabled': True,
            'pools': {
                'tank1': {
                    'type': 'raidz',
                    'devices': ['/dev/sdb', '/dev/sdc', '/dev/sdd'],
                    'mounts': {
                        '/data': {},
                        '/home': {},
                        '/minio': {},
                    },
                },
                'tank2': {
                    'type': 'raidz',
                    'devices': ['/dev/sde', '/dev/sdf', '/dev/sdg'],
                    'mounts': {
                        '/backup': {},
                        # '/backup/fire.hm.benjamin-borbe.de': {},
                    },
                },
            },
        },
    },
}
