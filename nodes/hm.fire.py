nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'kvm': True,
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': [
                # allow forward
                'iptables -A FORWARD -j ACCEPT',
                # drop noise
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 67 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 68 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 137 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 138 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol tcp --dport 443 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 1947 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 8612 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol udp --dport 17500 -j DROP',
                'iptables -A INPUT -m state --state NEW --protocol tcp --dport 17500 -j DROP',
                'iptables -A INPUT -j DROP -d 224.0.0.0/24',
            ],
        },
    },
}
