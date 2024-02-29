@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if metadata.get('kvm', {}).get('enabled', False):
        pkgs_install = (
            'cpu-checker',
            'qemu-system-x86',
            'libvirt-daemon-system',
            'libvirt-clients',
            'bridge-utils',
            'virtinst',
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
