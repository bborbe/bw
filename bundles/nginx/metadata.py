@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('nginx', {}).get('enabled', False):
        for name, data in metadata.get('nginx', {}).get('vhosts', {}).items():
            rules.add('-A INPUT -m state --state NEW -p tcp --dport {} -j ACCEPT'.format(data.get('port', 80)))
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    result = {
        'apt': {
            'packages': {}
        }
    }
    if metadata.get('nginx', {}).get('enabled', False):
        pkgs_install = (
            'apache2-utils',
            'nginx',
        )
        for package_name in pkgs_install:
            result['apt']['packages'][package_name] = {
                'installed': True
            }
    return result
