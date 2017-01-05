if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

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
