nodes['nc.v22016124049440903'] = {
    'hostname': 'v22016124049440903.goodsrv.de',
    'groups': {
        'ubuntu-bionic',
    },
    'metadata': {
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'version': '1.15.6',
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
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 587 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 993 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 2222 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 3128 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 6443 -j ACCEPT',
                    '-A INPUT -p tcp -m state --state NEW -m tcp --dport 64738 -j ACCEPT',
                },
            },
        },
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '185.170.112.48',
                    'netmask': '255.255.252.0',
                    'gateway': '185.170.112.1',
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
