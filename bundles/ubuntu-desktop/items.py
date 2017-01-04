os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'ubuntu-desktop': {},
    'gnome-terminal': {},
    'software-center': {},
    'unity-lens-applications': {},
    'indicator-session': {},
}
