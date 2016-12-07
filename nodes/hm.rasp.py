nodes['hm.rasp'] = {
    'hostname': 'rasp.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'openvpn': True,
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
                # drop noise
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
