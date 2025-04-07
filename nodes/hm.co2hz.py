import bwtv as teamvault

nodes['hm.co2hz'] = {
    'hostname': 'co2hz.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'backup_client': {
            'enabled': True,
        },
        'co2mon': {
            'enabled': True,
            'mqtt-host': 'rasp4.hm.benjamin-borbe.de',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            'mqtt-queue': 'sensors',
            'co2-name': 'co2hz/co2',
            'temperatur-name': 'co2hz/temperatur',
            'device': '/dev/co2mini0',
        },
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'version': '1.24.2',
            'os': 'linux',
        },
        'iptables': {
            'enabled': True,
        },
    },
}
