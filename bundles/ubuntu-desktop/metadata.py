@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    result = {
        'apt': {
            'packages': {}
        }
    }

    for package_name in (
        'gedit',
        'gnome-terminal',
        'tk-dev',
        'ubuntu-desktop',
        'gnome-tweaks',
        'fonts-dejavu-core',
        'fonts-dejavu',
        'fonts-ubuntu',
        'fonts-noto-mono',
        'gdm3',
    ):
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('ubuntu-desktop', {}).get('enabled', False)
        }

    if metadata.get('ubuntu-desktop', {}):
        for package_name in (
            'build-essential',
            'gnome-tweaks',
            'libbz2-dev',
            'libffi-dev',
            'libldap2-dev',
            'liblzma-dev',
            'libncursesw5-dev',
            'libreadline-dev',
            'libsasl2-dev',
            'libsqlite3-dev',
            'libssl-dev',
            'libxml2-dev',
            'libxml2-utils',
            'libxmlsec1-dev',
            'python3-dev',
            'python3-venv',
            'rsync',
            'unixodbc-dev',
            'unzip',
            'xz-utils',
            'zlib1g-dev',
        ):
            result['apt']['packages'][package_name] = {
                'installed': True,
            }
    return result
