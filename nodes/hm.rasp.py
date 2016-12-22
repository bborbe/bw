nodes['hm.rasp'] = {
    'hostname': 'rasp.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'debian',
        'release': 'jessie',
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.2',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
        },
        'openvpn': {
            'enabled': True,
        },
        'cron': {
            'jobs': {
                'dns-update': '* * * * * root /root/scripts/dns-update-home.benjamin-borbe.de.sh > /dev/null',
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': [
                # allow openvpn
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',
                # allow forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',
            ],
        },
    },
}
