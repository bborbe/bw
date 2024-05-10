@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if metadata.get('kvm-guest', {}).get('enabled', False):
        pkgs_install = (
            'acpi',
            'acpid',
            'qemu-guest-agent',
        )
        result = {
            'apt': {
                'packages': {}
            }
        }
        for package_name in pkgs_install:
            result['apt']['packages'][package_name] = {
                'installed': True
            }
        return result
    return {}
