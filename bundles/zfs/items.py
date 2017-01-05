if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}
pkg_apt = {}

pkg_apt['zfsutils-linux'] = {
    'installed': node.metadata.get('zfs', {}).get('enabled', False),
}

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
        parts = ['zfs create -p']
        parts.append('-o mountpoint={mount}'.format(mount=name))
        if data.get('sharenfs', False):
            parts.append('-o sharenfs=on'.format(mount=name))
        parts.append('storage{mount}'.format(mount=name))
        cmd = ' '.join(parts)
        actions['zfs_mount_{mount}'.format(mount=name)] = {
            'unless': 'zfs list storage{mount}'.format(mount=name),
            'command': 'rm -rf {mount} && {cmd}'.format(mount=name, cmd=cmd),
            'needs': ['action:zpool_create_storage'],
            'needed_by': ['svc_systemd:'],
        }
