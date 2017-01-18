nodes['sm.tools'] = {
    'hostname': 'tools.seibert-media.net',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'hosts': {
            'ipv4': {
                '138.201.37.217': ['tools.seibert-media.net', 'tools'],
            },
            'ipv6': {
                '2a01:4f8:171:3957::2': ['tools.seibert-media.net'],
            },
        },
        'kvm': {
            'enabled': True,
        },
        'grub': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['eth0'],
            'rules': {
                'nat': [
                    # OpenVpn
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 563 -j DNAT --to-destination 172.16.10.3:563',
                    # Http + Https
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 80 -j DNAT --to-destination 172.16.10.2:1080',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 443 -j DNAT --to-destination 172.16.10.2:1443',
                    # Minecraft
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 20001 -j DNAT --to-destination 172.16.11.15:30000',
                    # Mumble
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 64738 -j DNAT --to-destination 172.16.11.15:30019',
                    # Smtp + Smtps
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 25 -j DNAT --to-destination 172.16.11.15:30025',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 465 -j DNAT --to-destination 172.16.11.15:30465',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 587 -j DNAT --to-destination 172.16.11.15:30587',
                    # Imap + Imaps
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 143 -j DNAT --to-destination 172.16.11.15:30143',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 993 -j DNAT --to-destination 172.16.11.15:30993',
                    # Ts3
                    '-A PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 9987 -j DNAT --to-destination 172.16.11.15:30087',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 10011 -j DNAT --to-destination 172.16.11.15:30111',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 30033 -j DNAT --to-destination 172.16.11.15:30033',
                    # Dns
                    '-A PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30053',
                    '-A PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30054',
                ],
                'filter': [
                    # Forward
                    '-A FORWARD -j ACCEPT',
                ],
            },
        },
        'users': {
            'bkendinibilir': {
                'enabled': True,
            },
            'kwiesmueller': {
                'enabled': True,
            },
            'mfrankl': {
                'enabled': True,
            },
            'mschnitzius': {
                'enabled': True,
            },
            'owolf': {
                'enabled': True,
            },
            'sjanusch': {
                'enabled': True,
            },
            'trehn': {
                'enabled': True,
            },
        },
    },
}
