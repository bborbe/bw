if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}

pkgs = (
    'chromium-browser',
    'firefox',
    'emacs',
    'gedit',
    'gnome-terminal',
    'indicator-session',
    'lightdm',
    'software-center',
    'ubuntu-desktop',
    'unity-lens-applications',
)

for pkg in pkgs:
    pkg_apt[pkg] = {
        'installed': node.metadata.get('ubuntu-desktop', {}).get('enabled', False),
    }
