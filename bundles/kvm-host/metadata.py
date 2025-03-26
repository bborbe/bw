@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('kvm-host', {}).get('enabled', False):
        return {}

    pkgs_install = (
        'bmon',
        'bridge-utils',
        'cloud-utils',
        'cpu-checker',
        'iotop',
        'iperf3',
        'libvirt-clients',
        'libvirt-daemon-system',
        'ovmf',
        'qemu-system-x86',
        'qemu-utils',
        'swtpm-tools',
        'sysstat',
        'virt-top',
        'virtinst',
        'whois',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs_install:
        result.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {}).setdefault('installed', True)
    return result


@metadata_reactor.provides(
    'sysctl/options',
)
def kvm_quest_sysctl(metadata):
    if metadata.get('kvm-host', {}).get('enabled', False):
        return {
            'sysctl': {
                'options': {
                    'vm.swappiness': '1',
                }
            }
        }
    return {}
