nodes['hz.hetzner-1'] = {
    'hostname': 'hetzner-1.benjamin-borbe.de',
    'groups': {
        'ubuntu-jammy',
    },
    'metadata': {
        'netplan': {
            'enabled': True,
            'ethernets': {
                'ens4': {
                    'dhcp4': True,
                    'dhcp6': False,
                },
            },
        },
        'nginx': {
            'enabled': True,
            'vhosts': {
                'kickstart': {
                    'ip': '159.69.203.89',
                    'root': '/var/lib/kickstart',
                    'locations': {
                        '/': {
                            'autoindex': 'on',
                        },
                    },
                    'server_names': [
                        'kickstart.benjamin-borbe.de',
                        'ks.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': False,
                        'cert': '/etc/letsencrypt/live/kickstart.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/kickstart.benjamin-borbe.de/privkey.pem',
                    },
                    'indexes': [],
                },
            },
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
