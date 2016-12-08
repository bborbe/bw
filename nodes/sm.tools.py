nodes['sm.tools'] = {
    'hostname': 'tools.seibert-media.net',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'kvm': True,
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['eth0'],
            'rules': [
                # OpenVpn
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 563 -j DNAT --to-destination 172.16.10.3:563',
                # Http + Https
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 80 -j DNAT --to-destination 172.16.10.2:1080',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 443 -j DNAT --to-destination 172.16.10.2:1443',
                # Minecraft
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 20001 -j DNAT --to-destination 172.16.11.15:30000',
                # Mumble
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 64738 -j DNAT --to-destination 172.16.11.15:30019',
                # Smtp + Smtps
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 25 -j DNAT --to-destination 172.16.11.15:30025',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 465 -j DNAT --to-destination 172.16.11.15:30465',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 587 -j DNAT --to-destination 172.16.11.15:30587',
                # Imap + Imaps
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 143 -j DNAT --to-destination 172.16.11.15:30143',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 993 -j DNAT --to-destination 172.16.11.15:30993',
                # Ts3
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 9987 -j DNAT --to-destination 172.16.11.15:30087',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 10011 -j DNAT --to-destination 172.16.11.15:30111',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 30033 -j DNAT --to-destination 172.16.11.15:30033',
                # Dns
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p udp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30053',
                'iptables -t nat -A CUSTOM-PREROUTING -i eth0 -p tcp -d 138.201.37.217 --dport 53 -j DNAT --to-destination 172.16.11.15:30054',
                # Forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',
            ],
        },
    },
}
