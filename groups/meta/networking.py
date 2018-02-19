groups['meta-networking'] = {
    'member_patterns': (
        r'.*',
    ),
    'metadata': {
        'networking': {
            'enabled': True,
            'nameservers': ['8.8.4.4', '8.8.8.8'],
        },
    },
}
