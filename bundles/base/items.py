os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'bash': {},
    'git': {},
    'iptables-persistent': {},
    'curl': {},
    'wget': {},
    'screen': {},
    'mailutils': {},
    'postfix': {},
    'augeas-tools': {},
    'monit': {},
    'zsh': {},
    'tmux': {},
    'vim': {},
}
