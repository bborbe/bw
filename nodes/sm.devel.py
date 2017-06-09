nodes['sm.devel'] = {
    'hostname': 'bborbe.devel.lf.seibert-media.net',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'docker': {
            'enabled': True,
        },
        'hosts': {
            'ipv4': {
                '10.1.6.16': ['bborbe.devel.lf.seibert-media.net', 'bborbe'],
            },
        },
        'networking': {
            'enabled': True,
            'nameservers': ['8.8.4.4', '8.8.8.8'],
            'interfaces': {
                'eth0': {
                    'address': '10.1.6.16',
                    'netmask': '255.255.255.0',
                    'gateway': '10.1.6.1',
                },
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': [
                    # Http + Https
                    '-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                    '-A INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
                ],
            },
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
        'tomcat7': {
            'enabled': True,
        },
    },
}
