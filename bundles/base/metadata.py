@metadata_processor
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
    )
    for package_name in pkgs_install:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {}).setdefault('installed', True)
    return metadata, DONE


@metadata_processor
def uninstall_apt_packages(metadata):
    pkgs_uninstall = (
        'mlocate',
    )
    for package_name in pkgs_uninstall:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {}).setdefault('installed', False)
    return metadata, DONE
