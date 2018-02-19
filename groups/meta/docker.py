import bwtv as teamvault

groups['meta-docker'] = {
    'member_patterns': (
        r'.*',
    ),
    'metadata': {
        'docker': {
            'login': {
                'docker.benjamin-borbe.de': {
                    'username': teamvault.username('7qGQOW', site='benjamin-borbe'),
                    'password': teamvault.password('7qGQOW', site='benjamin-borbe'),
                },
            },
        },
    },
}
