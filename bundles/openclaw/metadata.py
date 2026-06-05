defaults = {
    'openclaw': {
        'enabled': False,
        'user': 'openclaw',
        'matrix': {
            'enabled': False,
            'homeserver': None,
            'user_id': None,
            'password': None,
        },
    },
}


@metadata_reactor.provides(
    'users',
)
def add_user(metadata):
    openclaw = metadata.get('openclaw', {})
    if not openclaw.get('enabled', False):
        return {}
    user = openclaw.get('user', 'openclaw')
    return {
        'users': {
            user: {
                'enabled': True,
            },
        },
    }


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('openclaw', {}).get('enabled', False):
        return {}

    pkgs_install = (
        'bat',
        'fd-find',
        'ffmpeg',
        'fzf',
        'gh',
        'jq',
        'ripgrep',
        'trash-cli',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs_install:
        result['apt']['packages'][package_name] = {
            'installed': True
        }
    return result
