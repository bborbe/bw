@metadata_reactor.provides(
    'zfs/pools',
)
def zfs_backup_volumes(metadata):
    backup_server = metadata.get('backup_server', {})
    pool = backup_server.get('pool', 'tank1')
    result = {
        'zfs': {
            'pools': {
                pool: {
                    'mounts': {}
                }
            }
        }
    }
    if backup_server.get('enabled', False) and metadata.get('zfs', {}).get('enabled', False):
        for name, data in backup_server.get('targets', {}).items():
            result['zfs']['pools'][pool]['mounts']['/backup/{}'.format(name)] = {}
    return result


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if metadata.get('backup_server', {}).get('enabled', False) is False:
        return {}
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in ['rsync']:
        result['apt']['packages'][package_name] = {
            'installed': True,
        }
    return result
