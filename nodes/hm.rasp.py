import bwtv as teamvault

nodes['hm.rasp'] = {
    'hostname': 'rasp.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'debian',
        'release': 'jessie',
        'networking': {
            'enabled': True,
            'nameservers': ['8.8.4.4', '8.8.8.8'],
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.2',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {
                'up route add -net 172.16.22.0/24 gw 172.16.23.3': {},
                'up route add -net 172.16.24.0/24 gw 172.16.23.5': {},
            },
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
                'filter': [
                    # allow openvpn
                    '-A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                ],
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
