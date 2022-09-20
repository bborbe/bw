
groups['raspbian'] = {
    'bundles': (
        'apt',
    ),
    'subgroup_patterns': (
        r"raspbian-.+",
    ),
    'os': 'raspbian',
    'metadata': {
        'os': 'raspbian',
    },
}

groups['raspbian-jessie'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (8, 0),
    'metadata': {
        'release': 'jessie',
    },
}

groups['raspbian-stretch'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (9, 0),
    'metadata': {
        'release': 'stretch',
    },
}

groups['raspbian-buster'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (10, 0),
    'metadata': {
        'release': 'buster',
    },
}

groups['raspbian-bullseye'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (11, 0),
    'metadata': {
        'release': 'bullseye',
    },
}
