defaults = {
    'hermes': {
        'enabled': False,
        'user': 'hermes',
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
    hermes = metadata.get('hermes', {})
    if not hermes.get('enabled', False):
        return {}
    user = hermes.get('user', 'hermes')
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
    if not metadata.get('hermes', {}).get('enabled', False):
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
