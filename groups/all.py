import bwtv as teamvault

groups['all'] = {
    'member_patterns': (
        r'.*',
    ),
    'bundles': (
        'authorized_key',
        'dotfiles',
        'git',
        'group',
        'user',
    ),
    'metadata': {
        'docker': {
            'login': {
                'docker.tools.seibert-media.net': {
                    'username': teamvault.username('7qGQOW', site='benjamin-borbe'),
                    'password': teamvault.password('7qGQOW', site='benjamin-borbe'),
                },
            },
        },
    },
}
