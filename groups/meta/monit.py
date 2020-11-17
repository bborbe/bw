import bwtv as teamvault

groups['meta-monit'] = {
    'subgroup_patterns': (
        r".+",
    ),
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
