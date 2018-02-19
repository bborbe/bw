import bwtv as teamvault

groups['meta-monit'] = {
    'members': [
        'hm.co2hz',
        'hm.co2wz',
        'hm.fire',
        'hm.rasp',
        'hm.nuke',
        'pn.sun',
    ],
    'metadata': {
        'monit': {
            'enabled': True,
            'mailserver': {
                'sender': teamvault.username('KwRoO7', site='benjamin-borbe'),
                'recipient': 'bborbe@rocketnews.de',
                'server': 'mail.benjamin-borbe.de',
                'port': 587,
                'username': teamvault.username('KwRoO7', site='benjamin-borbe'),
                'password': teamvault.password('KwRoO7', site='benjamin-borbe'),
            },
        },
    },
}
