@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs_install = [
        'augeas-tools',
        'bash',
        'bind9-dnsutils',
        'ca-certificates',
        'curl',
        'ethtool',
        'file',
        'iproute2',
        'iputils-ping',
        'locales',
        'mailutils',
        'make',
        'net-tools',
        'nfs-common',
        'openssh-client',
        'psmisc',
        'python-is-python3',
        'rsync',
        'screen',
        'tmux',
        'vim',
        'wget',
        'zsh',
    ]
    
    # Only install postfix if msmtp is not enabled (avoid MTA conflict)
    if not metadata.get('msmtp', {}).get('enabled', False):
        pkgs_install.append('postfix')
    
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs_install:
        result['apt']['packages'][package_name] = {
            'installed': True
        }
    
    # Explicitly remove postfix when msmtp is enabled
    if metadata.get('msmtp', {}).get('enabled', False):
        result['apt']['packages']['postfix'] = {
            'installed': False
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


@metadata_reactor.provides(
    'git/clones/scripts',
)
def git_clone_scripts(metadata):
    return {
        'git': {
            'clones': {
                'scripts': {
                    'repo': 'https://github.com/bborbe/scripts.git',
                    'target': '/root/scripts',
                },
            },
        },
    }
