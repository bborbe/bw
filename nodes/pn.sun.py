nodes['pn.sun'] = {
    'hostname': 'sun.pn.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'networking': {
            'enabled': True,
            'interfaces': {
                'eth0': {
                    'dns-nameservers': '8.8.4.4 8.8.8.8',
                },
                'br0': {
                    'address': '192.168.2.3',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.2.1',
                    'bridge_ports': 'eth0',
                    'bridge_stp': 'on',
                    'bridge_fd': '0',
                    'bridge_maxwait': '0',
                },
                'fw-host': {
                    'address': '172.16.70.1',
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
                'up route add -net 172.16.71.0/24 gw 172.16.70.5': {},
                'up route add -net 172.16.72.0/24 gw 172.16.70.5': {},
            },
        },
        'dns-update': {
            'enabled': True,
            'updates': {
                'pn.benjamin-borbe.de': {
                    'zone': 'benjamin-borbe.de',
                    'node': 'pn',
                    'dns-server': 'ns.rocketsource.de',
                    'ip-url': 'https://ip.benjamin-borbe.de',
                    'private': teamvault.file('aL50O8', site='benjamin-borbe'),
                    'key': teamvault.file('9L64w3', site='benjamin-borbe'),
                },
            },
        },
        'openvpn': {
            'enabled': True,
        },
        'kvm': {
            'enabled': True,
        },
        'grub': {
            'enabled': True,
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['br0'],
            'rules': {
                'filter': [
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                ],
            },
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
    },
}
