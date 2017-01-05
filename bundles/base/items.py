if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'bash': {},
    'curl': {},
    'wget': {},
    'screen': {},
    'mailutils': {},
    'postfix': {},
    'augeas-tools': {},
    'tmux': {},
    'vim': {},
    'net-tools': {},
    'iproute2': {},
    'ca-certificates': {},
    'iputils-ping': {},
    'openssh-client': {},
    'rsync': {},
    'nfs-common': {},
}

if node.os == 'ubuntu':
    pkg_apt['mountall'] = {}
