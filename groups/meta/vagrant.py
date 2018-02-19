groups['meta-vagrant'] = {
    'member_patterns': (
        r'.*vagrant.*',
    ),
    'metadata': {
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'nat': {
                    # SSH
                    '-A PREROUTING -p tcp --dport 2222 -j DNAT --to-destination 127.0.0.1:22',
                },
            },
        },
        'users': {
            'vagrant': {
                'sudo': True,
                'enabled': True,
            },
        },
    },
}
