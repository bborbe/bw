if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

for username, data in node.metadata['users'].items():
    homedir = data.get('home', '/home/{}'.format(username))
    dotfiles = data.get('dotfiles', '')
    if len(dotfiles) > 0:
        actions = {
            'checkout_dotfiles_{}'.format(username): {
                'unless': 'test -e {}/dotfiles'.format(homedir),
                'command': 'git clone {} {}/dotfiles && chown -R {}:{} {}/dotfiles'.format(dotfiles, homedir, username, username, homedir),
                'needs': ['pkg_apt:git'],
            }
        }
