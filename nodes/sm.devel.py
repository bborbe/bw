nodes['sm.devel'] = {
    'hostname': 'bborbe.devel.lf.seibert-media.net',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': [
                # Http + Https
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
            ],
        },
    },
}
