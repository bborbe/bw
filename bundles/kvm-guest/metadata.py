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
                    'fs.inotify.max_queued_events': '2099999999'
                }
            }
        }
    return {}
