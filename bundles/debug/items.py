if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {
    'atop': {
        'installed': False,
    },
}

debugs_pkgs = (
    'bmon',
    'bonnie++',
    'dnsutils',
    'iotop',
    'psmisc',
    'sysstat',
    'telnet',
    'traceroute',
    'iputils-tracepath',
)

if node.metadata.get('debug', {}).get('enabled', False):
    for pkg in debugs_pkgs:
        pkg_apt.setdefault(pkg, {}).setdefault('installed', True)
