import bwtv as teamvault

nodes['hm.co2wz'] = {
    'hostname': 'co2wz.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'backup_client': {
            'enabled': True,
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'addresses': ['192.168.178.7/24'],
                    'routes': [
                        {
                            'to': '0.0.0.0/0',
                            'via': '192.168.178.1',
                        }
                    ],
                    'nameservers': ['8.8.8.8', '8.8.4.4'],
                },
            },
        },
        'co2mon': {
            'enabled': True,
            'mqtt-host': 'rasp4.hm.benjamin-borbe.de',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            'mqtt-queue': 'sensors',
            'co2-name': 'co2wz/co2',
            'temperatur-name': 'co2wz/temperatur',
            'device': '/dev/co2mini0',
        },
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'version': '1.16.4',
            'os': 'linux',
        },
        'iptables': {
            'enabled': True,
        },
    },
}
