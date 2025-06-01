groups['ubuntu'] = {
    'bundles': (
        'apt',
        'ubuntu',
    ),
    'subgroup_patterns': (
        r"ubuntu-.+",
    ),
    'os': 'ubuntu',
    'metadata': {
        'os': 'ubuntu',
        'grub': {
            'enabled': True,
        },
        'kernel_modules': {
            'lp': {},
            'loop': {},
        },
        'apt': {
            'packages': {
                'unattended-upgrades': {
                    'installed': True,
                }
            },
        },
    },
}

groups['ubuntu-xenial'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (16, 4),
    'metadata': {
        'release': 'xenial',
    },
}

groups['ubuntu-bionic'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (18, 4),
    'metadata': {
        'release': 'bionic',
    },
}

groups['ubuntu-focal'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (20, 4),
    'metadata': {
        'release': 'focal',
    },
}

groups['ubuntu-jammy'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (22, 4),
    'metadata': {
        'release': 'jammy',
    },
}

groups['ubuntu-noble'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (24, 4),
    'metadata': {
        'release': 'noble',
    },
}
