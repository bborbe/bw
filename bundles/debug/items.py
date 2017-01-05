if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}

if node.metadata.get('debug', {}).get('enabled', False):
    pkg_apt.setdefault('telnet', {}).setdefault('installed', True)
    pkg_apt.setdefault('dnsutils', {}).setdefault('installed', True)
    pkg_apt.setdefault('traceroute', {}).setdefault('installed', True)
    pkg_apt.setdefault('psmisc', {}).setdefault('installed', True)
    pkg_apt.setdefault('sysstat', {}).setdefault('installed', True)
    pkg_apt.setdefault('atop', {}).setdefault('installed', True)
    pkg_apt.setdefault('iotop', {}).setdefault('installed', True)
    pkg_apt.setdefault('bonnie++', {}).setdefault('installed', True)
