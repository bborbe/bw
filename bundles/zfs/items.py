os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

pkg_apt = {
    'zfsutils-linux': {
        'installed': node.metadata.get('zfs', {}).get('enabled', False),
    },
}

actions = {}

if node.metadata.get('zfs', {}).get('enabled', False):
    zfs_device = node.metadata.get('zfs', {}).get('device', ''),
    if len(zfs_device) == 0:
        raise Exception('zfs device missing')
    actions['zpool_create_storage'] = {
        'unless': 'zpool status storage',
        'command': 'zpool create storage {device}'.format(device=zfs_device),
        'needs': ['pkg_apt:zfsutils-linux'],
        'needed_by': ['svc_systemd:'],
    }
    for name, data in node.metadata.get('zfs', {}).get('mounts', {}).items():
        actions['zfs_mount_{mount}'.format(mount=name)] = {
            'unless': 'zfs list storage{mount}'.format(mount=name),
            'command': 'rm -rf {mount} && zfs create -p -o mountpoint={mount} storage{mount}'.format(mount=name),
            'needs': ['action:zpool_create_storage'],
            'needed_by': ['svc_systemd:'],
        }
