nodes['hz.hetzner-1'] = {
    'hostname': 'hetzner-1.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'nginx': {
            'enabled': True,
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.16.4',
            'os': 'linux',
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 25 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 53 -j ACCEPT',
                    '-A INPUT -p udp -m state --state NEW -m udp --dport 53 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 143 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 465 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 563 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 587 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 993 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 2222 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 3128 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 6443 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 64738 -j ACCEPT',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
            },
        },
    },
}
