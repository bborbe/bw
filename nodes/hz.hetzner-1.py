nodes['hz.hetzner-1'] = {
    'hostname': 'hetzner-1.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'conduit-server': {
            'enabled': True,
            'server_name': 'matrix.benjamin-borbe.de',
            'well_known_base_domain': 'benjamin-borbe.de',
            'well_known_ip': '159.69.203.89',
        },
        'docker': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': True,
                    'dhcp6': False,
                },
            },
        },
        'screego': {
            'enabled': True,
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
                'matrix': {
                    'ip': '159.69.203.89',
                    'server_names': [
                        'matrix.benjamin-borbe.de',
                    ],
                    'ssl': {
                        'force': True,
                        'cert': '/etc/letsencrypt/live/matrix.benjamin-borbe.de/fullchain.pem',
                        'key': '/etc/letsencrypt/live/matrix.benjamin-borbe.de/privkey.pem',
                    },
                    'locations': {
                        '/': {
                            'proxy_pass': 'http://127.0.0.1:8448',
                            'proxy_set_header Host': '$host',
                            'proxy_set_header X-Real-IP': '$remote_addr',
                        },
                    },
                    'indexes': [],
                },
            },
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    # '-A FORWARD -j ACCEPT',
                    # '-A FORWARD -i tun0 -o tun0 -j DROP',
                    '-A FORWARD -i tun0 -o eth0 -j ACCEPT',
                    '-A FORWARD -i eth0 -o tun0 -m state --state RELATED,ESTABLISHED -j ACCEPT',
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
