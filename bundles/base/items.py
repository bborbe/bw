if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}

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

pkgs_uninstall = (
    'mlocate',
)

for pkg in pkgs_install:
    pkg_apt[pkg] = {
        'installed': True,
    }

for pkg in pkgs_uninstall:
    pkg_apt[pkg] = {
        'installed': False,
    }

if node.os == 'ubuntu':
    pkg_apt['mountall'] = {}
