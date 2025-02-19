@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs_install = (
        'augeas-tools',
        'bash',
        'bind9-dnsutils',
        'ca-certificates',
        'curl',
        'file',
        'iproute2',
        'iputils-ping',
        'locales',
        'mailutils',
        'make',
        'net-tools',
        'nfs-common',
        'openssh-client',
        'postfix',
        'psmisc',
        'python-is-python3',
        'rsync',
        'screen',
        'tmux',
        'vim',
        'wget',
        'zsh',
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

@metadata_reactor.provides(
    'apt/packages',
)
def uninstall_apt_packages(metadata):
    return {
        'apt': {
            'packages': {
                'mlocate': {
                    'installed': False
                }
            }
        }
    }
