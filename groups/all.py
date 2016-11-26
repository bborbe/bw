groups['all'] = {
    'member_patterns': (
        r'.*',
    ),
    'bundles': (
        'base',
        'sudo',
        'backup',
        'monit',
    ),
    'metadata': {
        'users': {
            "bborbe": {
                'sudo': True,
            },
            "root": {
            },
        },
    },
}
