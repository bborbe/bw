groups['ubuntu'] = {
    'members_add': lambda node: node.metadata.get('os') == 'ubuntu',
    'bundles': (
        'apt',
    ),
    'os': 'ubuntu',
}

groups['ubuntu-xenial'] = {
    'members_add': lambda node: node.metadata.get('os') == 'ubuntu' and node.metadata.get('release') == 'xenial',
    'bundles': (
        'systemd',
    ),
    'os_version': (16, 4),
    'metadata': {
        'apt': {
            'packages': {
                'linux-image-virtual-lts-xenial': {},
                'linux-image-extra-virtual-lts-xenial': {},
            },
        },
    },
}

groups['ubuntu-bionic'] = {
    'members_add': lambda node: node.metadata.get('os') == 'ubuntu' and node.metadata.get('release') == 'bionic',
    'bundles': (
        'systemd',
    ),
    'os_version': (18, 4),
    'metadata': {
        'apt': {
            'packages': {
                'linux-image-virtual': {},
                'linux-image-extra-virtual': {},
            },
        },
    },
}

groups['ubuntu-focal'] = {
    'members_add': lambda node: node.metadata.get('os') == 'ubuntu' and node.metadata.get('release') == 'focal',
    'bundles': (
        'systemd',
    ),
    'os_version': (20, 4),
    'metadata': {
        'apt': {
            'packages': {
                'linux-image-virtual': {},
                'linux-image-extra-virtual': {},
            },
        },
    },
}

groups['debian'] = {
    'members_add': lambda node: node.metadata.get('os') == 'debian',
    'bundles': (
        'apt',
    ),
    'os': 'debian',
}

groups['debian-jessie'] = {
    'members_add': lambda node: node.metadata.get('os') == 'debian' and node.metadata.get('release') == 'jessie',
    'bundles': (
        'systemd',
    ),
    'os_version': (8, 0),
}

groups['debian-stretch'] = {
    'members_add': lambda node: node.metadata.get('os') == 'debian' and node.metadata.get('release') == 'stretch',
    'bundles': (
        'systemd',
    ),
    'os_version': (9, 0),
}


groups['debian-buster'] = {
    'members_add': lambda node: node.metadata.get('os') == 'debian' and node.metadata.get('release') == 'buster',
    'bundles': (
        'systemd',
    ),
    'os_version': (10, 0),
}


groups['raspbian'] = {
    'members_add': lambda node: node.metadata.get('os') == 'raspbian',
    'bundles': (
        'apt',
    ),
    'os': 'raspbian',
}

groups['raspbian-jessie'] = {
    'members_add': lambda node: node.metadata.get('os') == 'raspbian' and node.metadata.get('release') == 'jessie',
    'bundles': (
        'systemd',
    ),
    'os_version': (8, 0),
}

groups['raspbian-stretch'] = {
    'members_add': lambda node: node.metadata.get('os') == 'raspbian' and node.metadata.get('release') == 'stretch',
    'bundles': (
        'systemd',
    ),
    'os_version': (9, 0),
}

groups['raspbian-buster'] = {
    'members_add': lambda node: node.metadata.get('os') == 'raspbian' and node.metadata.get('release') == 'buster',
    'bundles': (
        'systemd',
    ),
    'os_version': (10, 0),
}

