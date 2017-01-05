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
