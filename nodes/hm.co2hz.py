import bwtv as teamvault

nodes['hm.co2hz'] = {
    'hostname': 'co2hz.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.6',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
        },
        'co2mon': {
            'enabled': True,
            'device': '/dev/co2mini0',
            'co2-name': 'HZ_CO2',
            'temperatur-name': 'HZ_TEMP',
            'mqtt-host': 'rasp3.hm.benjamin-borbe.de',
            'mqtt-queue': 'co2mon',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
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
