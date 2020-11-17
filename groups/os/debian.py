
groups['debian'] = {
    'bundles': (
        'apt',
    ),
    'os': 'debian',
    'subgroup_patterns': (
        r"debian-.+",
    ),
    'metadata': {
        'os': 'debian',
    },
}

groups['debian-jessie'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (8, 0),
    'metadata': {
        'release': 'jessie',
    },
}

groups['debian-stretch'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (9, 0),
    'metadata': {
        'release': 'stretch',
    },
}

groups['debian-buster'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (10, 0),
    'metadata': {
        'release': 'buster',
    },
}
