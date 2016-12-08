nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'openvpn': True,
        'kvm': True,
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['br0'],
            'rules': [
                # allow forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',
            ],
        },
    },
}
