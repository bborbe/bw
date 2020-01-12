import bwtv as teamvault

nodes['hm.co2wz'] = {
    'hostname': 'co2wz.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'raspbian',
        'release': 'stretch',
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
            'device': '/dev/co2mini0',
            'co2-name': 'WZ_CO2',
            'temperatur-name': 'WZ_TEMP',
            'mqtt-host': 'rasp.hm.benjamin-borbe.de',
            'mqtt-queue': 'co2mon',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
        },
        'iptables': {
            'enabled': True,
        },
    },
}
