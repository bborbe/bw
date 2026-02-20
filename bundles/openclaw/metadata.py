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
