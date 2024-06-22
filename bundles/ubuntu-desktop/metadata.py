@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'build-essential',
        'curl',
        'curl',
        'gedit',
        'gnome-terminal',
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
        'tk-dev',
        'ubuntu-desktop',
        'unixodbc-dev',
        'unzip',
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
