groups['ubuntu'] = {
    'bundles': (
        'apt',
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
    },
}

groups['ubuntu-xenial'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (16, 4),
}

groups['ubuntu-bionic'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (18, 4),
}

groups['ubuntu-focal'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (20, 4),
}

groups['ubuntu-jammy'] = {
    'bundles': (
        'systemd',
    ),
    'os_version': (20, 4),
}
