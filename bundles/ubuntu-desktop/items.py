os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if not (os == 'ubuntu' and release == 'xenial' or os == 'debian' and release == 'jessie'):
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {}

pkg_apt['ubuntu-desktop'] = {
    'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
}

pkg_apt['gnome-terminal'] = {
    'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
}

pkg_apt['software-center'] = {
    'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
}

pkg_apt['unity-lens-applications'] = {
    'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
}

pkg_apt['indicator-session'] = {
    'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
}
