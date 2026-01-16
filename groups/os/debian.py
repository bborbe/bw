
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

groups['debian-bullseye'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (11, 0),
    'metadata': {
        'release': 'bullseye',
    },
}

groups['debian-bookworm'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (12, 0),
    'metadata': {
        'release': 'bookworm',
    },
}

groups['debian-trixie'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (13, 0),
    'metadata': {
        'release': 'trixie',
    },
}
