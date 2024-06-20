@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'gedit',
        'gnome-terminal',
        'ubuntu-desktop',
        'unzip',
        'build-essential',
        'curl',
        'libbz2-dev',
        'libffi-dev',
        'liblzma-dev',
        'libncursesw5-dev',
        'libreadline-dev',
        'libsqlite3-dev',
        'libssl-dev',
        'libxml2-dev',
        'libxmlsec1-dev',
        'tk-dev',
        'xz-utils',
        'zlib1g-dev',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('ubuntu-desktop', {}).get('enabled', False)
        }
    return result
