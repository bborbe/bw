import bwtv as teamvault

nodes['hm.rasp3'] = {
    'hostname': 'rasp3.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-stretch',
    },
    'metadata': {
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'version': '1.15.6',
            'os': 'linux',
        },
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.2',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
        'mosquitto': {
            'enabled': True,
            'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                },
            },
        },
        'dns-update': {
            'enabled': True,
            'updates': {
                'home.benjamin-borbe.de': {
                    'zone': 'benjamin-borbe.de',
                    'node': 'home',
                    'dns-server': 'ns.rocketsource.de',
                    'ip-url': 'https://ip.benjamin-borbe.de',
                    'private': teamvault.file('aL50O8', site='benjamin-borbe'),
                    'key': teamvault.file('9L64w3', site='benjamin-borbe'),
                },
                'home.rocketnews.de': {
                    'zone': 'rocketnews.de',
                    'node': 'home',
                    'dns-server': 'ns.rocketsource.de',
                    'ip-url': 'https://ip.benjamin-borbe.de',
                    'private': teamvault.file('aL50O8', site='benjamin-borbe'),
                    'key': teamvault.file('9L64w3', site='benjamin-borbe'),
                },
            },
        },
    },
}
