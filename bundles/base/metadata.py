@metadata_reactor
def install_apt_packages(metadata):
    pkgs_install = (
        'augeas-tools',
        'bash',
        'ca-certificates',
        'curl',
        'file',
        'iproute2',
        'iputils-ping',
        'locale',
        'mailutils',
        'net-tools',
        'nfs-common',
        'openssh-client',
        'postfix',
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


@metadata_reactor
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
