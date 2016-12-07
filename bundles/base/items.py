os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
    'telnet': {},
    'dnsutils': {},
    'traceroute': {},
    'iputils-ping': {},
    'openssh-client': {},
    'mountall': {},
    'rsync': {},
    'nfs-common': {},
}
