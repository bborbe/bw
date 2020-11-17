@metadata_reactor
def zfs_backup_volumes(metadata):
    result = {
        'zfs': {
            'pools': {
                'tank1': {
                    'mounts': {}
                }
            }
        }
    }
    if metadata.get('backup_server', {}).get('enabled', False) and metadata.get('zfs', {}).get('enabled', False):
        for name, data in metadata.get('backup_server', {}).get('targets', {}).items():
            result['zfs']['pools']['tank1']['mounts']['/backup/{}'.format(name)] = {}
    return result
