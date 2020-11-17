@metadata_reactor
def install_apt_packages(metadata):
    pkgs_install = (
        'bash',
        'curl',
        'wget',
        'screen',
        'mailutils',
        'postfix',
        'augeas-tools',
        'tmux',
        'vim',
        'net-tools',
        'iproute2',
        'ca-certificates',
        'iputils-ping',
        'openssh-client',
        'rsync',
        'nfs-common',
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
