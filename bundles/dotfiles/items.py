os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

for username, data in node.metadata['users'].items():
    homedir = data.get('home', '/home/{}'.format(username))
    dotfiles = data.get('dotfiles', '')
    if len(dotfiles) > 0:
        actions = {
            'checkout_dotfiles_{}'.format(username): {
                'unless': 'test -e {}/dotfiles'.format(homedir),
                'command': 'git clone {} {}/dotfiles && chown -R {}:{} {}/dotfiles'.format(dotfiles, homedir, username, username, homedir),
                'needs': ["pkg_apt:git"],
            }
        }
