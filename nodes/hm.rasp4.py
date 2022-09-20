import bwtv as teamvault

nodes['hm.rasp4'] = {
    'hostname': 'rasp4.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'controller': {
            'enabled': True,
        },
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'version': '1.16.4',
            'os': 'linux',
        },
        'networking': {
            'interfaces': {
                'eth0': {
                    'address': '192.168.178.8',
                    'netmask': '255.255.255.0',
                    'gateway': '192.168.178.1',
                },
            },
            'routes': {},
        },
    },
}
