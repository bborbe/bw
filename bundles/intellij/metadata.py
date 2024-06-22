@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'libfuse2',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('intellij', {}).get('enabled', False)
        }
    return result


@metadata_reactor.provides(
    'sysctl/options',
)
def kvm_quest_sysctl(metadata):
    if metadata.get('intellij', {}).get('enabled', False):
        return {
            'sysctl': {
                'options': {
                    'fs.inotify.max_user_watches': '1048576',

                }
            }
        }
    return {}
