actions = {
    'apt_update': {
        'command': "apt-get update",
        'needed_by': ["pkg_apt:"],
        'triggered': True,
        'cascade_skip': False,
    },
}
