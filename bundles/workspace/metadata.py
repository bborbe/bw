@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('workspace', {}).get('enabled', False):
        return {}

    pkgs_install = (
        'gnupg2',
        'pinentry-tty',
        'build-essential',
        'libssl-dev',
        'zlib1g-dev',
        'libbz2-dev',
        'libreadline-dev',
        'libsqlite3-dev',
        'wget',
        'curl',
        'llvm',
        'xz-utils',
        'libxml2-dev',
        'libxmlsec1-dev',
        'libffi-dev',
        'liblzma-dev',
        'git',
        'keychain',
        'direnv',
        'ripgrep',
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
