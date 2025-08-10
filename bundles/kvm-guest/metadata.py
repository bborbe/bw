@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('kvm-guest', {}).get('enabled', False):
        return {}

    pkgs_install = (
        'acpi',
        'acpid',
        'bmon',
        'iotop',
        'qemu-guest-agent',
        'sysstat',
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
    if metadata.get('kvm-guest', {}).get('enabled', False):
        return {
            'sysctl': {
                'options': {
                    'fs.inotify.max_user_watches': '2099999999',
                    'fs.inotify.max_user_instances': '2099999999',
                    'fs.inotify.max_queued_events': '2099999999',
                    'net.ipv4.tcp_fin_timeout': '30',
                    'net.ipv4.tcp_tw_reuse': '2',
                    'net.ipv4.tcp_max_tw_buckets': '65536',
                }
            }
        }
    return {}
