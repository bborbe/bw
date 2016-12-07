nodes['nc.v22016124049440903'] = {
    'hostname': 'v22016124049440903.goodsrv.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'docker': True,
        'kubernetes': True,
        'openvpn': True,
        'zfs': {
            'enabled': True,
            'device': '/dev/sda4',
            'mounts': {
                '/var/lib/kubelet': {},
                '/var/lib/docker': {},
            },
        },
        'haproxy': {
            'ip': '185.170.112.48',
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
            'email': 'bborbe@rocketnews.de',
            'domains': {
                'benjamin-borbe.de': ['www.benjamin-borbe.de', 'test.benjamin-borbe.de', 'slideshow.benjamin-borbe.de'],
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['ens3'],
            'rules': [
                # Http + Https
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol tcp --dport 80 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol tcp --dport 443 -j ACCEPT',
                # K8s
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol tcp --dport 6443 -j ACCEPT',
                # allow forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',
                # drop noise
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 67 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 68 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 137 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 138 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol tcp --dport 443 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 1947 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 8612 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol udp --dport 17500 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW --protocol tcp --dport 17500 -j DROP',
                'iptables -A CUSTOM-INPUT -j DROP -d 224.0.0.0/24',
            ],
        },
    },
}
