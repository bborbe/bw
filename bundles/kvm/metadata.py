@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if metadata.get('kvm', {}).get('enabled', False):
        pkgs_install = (
            'bridge-utils',
            'cloud-utils',
            'cpu-checker',
            'libvirt-clients',
            'libvirt-daemon-system',
            'qemu-system-x86',
            'qemu-utils',
            'virtinst',
            'whois',
            'virt-top',
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
