@metadata_processor
def zfs_backup_volumes(metadata):
    if metadata.get('backup_server', {}).get('enabled', False) and metadata.get('zfs', {}).get('enabled', False):
        targets = metadata.get('backup_server', {}).get('targets', {})
        mounts = metadata.setdefault('zfs', {}).setdefault('pools', {}).setdefault('tank1', {}).setdefault('mounts', {})
        for name, data in targets.items():
            mounts['/backup/{}'.format(name)] = {}
    return metadata, DONE
