nodes['hm.nuke-boss'] = {
    'hostname': 'nuke-boss.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'workspace': {
            'enabled': True,
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
                    '-A INPUT -m state --state NEW -p tcp --dport 18789 -j ACCEPT',
                    # '-A INPUT -j ACCEPT',
                    # '-A FORWARD -j ACCEPT',
                }),
            },
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'optional': True,
                    'match': {'name': 'en*'},
                    'set-name': 'eth0',
                    'addresses': ['192.168.178.30/24'],
                    'routes': [{'to': 'default', 'via': '192.168.178.1'}],
                    'nameservers': {
                        'addresses': ['8.8.8.8', '8.8.4.4'],
                        'search': ['hm.benjamin-borbe.de'],
                    },
                },
            },
        },
        'users': {
            'bborbe': {'enabled': True, 'groups': ['sudo']},
            'openclaw': {'enabled': True},
            'install': {'enabled': False},
        },
    },
}
