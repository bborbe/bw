import bwtv as teamvault

nodes['hm.rasp'] = {
    'hostname': 'rasp.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'raspbian',
        'release': 'stretch',
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
        'nginx': {
            'enabled': True,
            'vhosts': {
                'openhab': {
                    'locations': {
                        '/': [
                            ('proxy_pass', 'http://localhost:8080/'),
                            ('proxy_set_header', 'Host $http_host'),
                            ('proxy_set_header', 'X-Real-IP $remote_addr'),
                            ('proxy_set_header', 'X-Forwarded-For $proxy_add_x_forwarded_for'),
                            ('proxy_set_header', 'X-Forwarded-Proto $scheme'),
                        ],
                    },
                },
            },
        },
        'openhab': {
            'enabled': True,
            'telegram': {
                'hausalertbot': {
                    'chatId': teamvault.username('pLvYPO', site='benjamin-borbe'),
                    'token': teamvault.password('pLvYPO', site='benjamin-borbe'),
                },
            },
            'mosquitto': {
                'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
                'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            },
        },
        'mosquitto': {
            'enabled': True,
            'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
        },
        'openvpn': {
            'enabled': True,
            'services': {
                'server': {
                    'enabled': True,
                },
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow openvpn
                    '-A INPUT -m state --state NEW -p tcp --dport 563 -j ACCEPT',
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
            },
        },
    },
}
