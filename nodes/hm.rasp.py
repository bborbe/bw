nodes['hm.rasp'] = {
    'hostname': 'rasp.hm.benjamin-borbe.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'openvpn': True,
        'cron': {
            'jobs': {
                'dns-update': '* * * * * root /root/scripts/dns-update-home.benjamin-borbe.de.sh > /dev/null',
            },
        },
    },
}
