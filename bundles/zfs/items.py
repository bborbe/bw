os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'zfsutils-linux': {
        'installed': node.metadata.get('zfs', False),
    },
    'mountall': {
        'installed': node.metadata.get('zfs', False),
    },
}

if node.metadata.get('zfs', False):
    zfs_device = node.metadata.get('zfs_device', '')
    if zfs_device:
        actions = {
            'zpool_create_storage': {
                'unless': 'zpool status storage',
                'command': 'zpool create storage {}'.format(zfs_device),
            },
        }
