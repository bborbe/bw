import bwtv as teamvault

groups['meta-monit'] = {
    'subgroup_patterns': (
        r".+",
    ),
    'metadata': {
        'monit': {
            'enabled': True,
            'mailserver': {
                'recipient': 'bborbe@rocketnews.de',
                'server': '172.16.90.1',
                'port': 25,
                'username': '',
                'password': '',
            },
        },
    },
}
