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
                # Drop noise
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 67 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 68 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 137 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 138 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 443 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 1947 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 8612 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p udp --dport 17500 -j DROP',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 17500 -j DROP',
                'iptables -A CUSTOM-INPUT -j DROP -d 224.0.0.0/24',
            ],
        },
    },
}
