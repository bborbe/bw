import bwtv as teamvault

nodes['hm.co2wz'] = {
    'hostname': 'co2wz.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.7',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
        'co2mon': {
            'enabled': True,
            'mqtt-host': 'rasp4.hm.benjamin-borbe.de',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            'mqtt-queue': 'co2mon',
            'co2-name': 'WZ_CO2',
            'temperatur-name': 'WZ_TEMP',
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
