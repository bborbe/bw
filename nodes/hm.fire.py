nodes['hm.fire'] = {
    'hostname': 'fire.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'networking': {
            'enabled': True,
            'interfaces': {
                'eth0': {
                    'pre-down': '/sbin/ethtool -s eth0 wol g',
                    'dns-search': 'hm.benjamin-borbe.de',
                    'dns-nameservers': '192.168.178.1',
                },
                'br0': {
                    'address': '192.168.178.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'br0:0': {
                    'address': '172.16.23.3',
                    'netmask': '255.255.255.0',
                },
                'fw-host': {
                    'address': '172.16.20.1',
                    'netmask': '255.255.255.0',
                    'pre-up': 'brctl addbr fw-host',
                    'post-down': 'brctl delbr fw-host',
                },
                'fw-freenas': {
                    'pre-up': 'brctl addbr fw-freenas',
                    'post-down': 'brctl delbr fw-freenas',
                },
                'fw-k8s': {
                    'pre-up': 'brctl addbr fw-k8s',
                    'post-down': 'brctl delbr fw-k8s',
                },
            },
            'routes': {
                'up route add -net 172.16.30.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.40.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.50.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.70.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.71.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.72.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.80.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.90.0/24 gw 172.16.23.2': {},
                'up route add -net 172.16.21.0/24 gw 172.16.20.2': {},
                'up route add -net 172.16.22.0/24 gw 172.16.20.2': {},
            },
        },
        'kvm': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': [
                # allow forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',
            ],
        },
    },
}
