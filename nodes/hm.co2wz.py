nodes['hm.co2wz'] = {
    'hostname': 'co2wz.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'debian',
        'release': 'stretch',
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.7',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {
                'up route add -net 172.16.0.0/12 gw 192.168.178.2': {},
                'up route add -net 192.168.2.0/24 gw 192.168.178.2': {},
            },
        },
        'co2mon': {
            'enabled': True,
            'device': '/dev/co2mini0',
            'openhab-url': 'http://rasp.hm.benjamin-borbe.de',
            'co2-name': 'WZ_CO2',
            'temperatur-name': 'WZ_TEMP',
            'humidity-name': 'WZ_HUM',
        },
        'iptables': {
            'enabled': True,
        },
    },
}
