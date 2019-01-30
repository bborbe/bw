if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}
pkg_apt = {}

pkg_apt['zfsutils-linux'] = {
    'installed': node.metadata.get('zfs', {}).get('enabled', False),
}

if node.metadata.get('zfs', {}).get('enabled', False):
    for pool_name, pool_data in node.metadata.get('zfs', {}).get('pools', {}).items():
        zfs_device = pool_data.get('devices', [])
        if len(zfs_device) == 0:
            raise Exception('zfs devices missing for pool {name}'.format(name=pool_name))

        zfs_type = pool_data.get('type', 'stripe')
        if not zfs_type in ('stripe', 'mirror', 'raidz', 'raidz2', 'raidz3'):
            raise Exception('zfs type invalid for pool {name}'.format(name=pool_name))
        if 'stripe' == zfs_type:
            zfs_type = ''

        actions['zpool_create_{name}'.format(name=pool_name)] = {
            'unless': 'zpool status {name}'.format(name=pool_name),
            'command': 'zpool create {name} {type} {device}'.format(name=pool_name, type=zfs_type, device=" ".join(zfs_device)),
            'needs': ['pkg_apt:zfsutils-linux'],
            'needed_by': ['svc_systemd:'],
        }

        for mount, data in pool_data.get('mounts', {}).items():
            parts = ['zfs create -p']
            parts.append('-o mountpoint={mount}'.format(mount=mount))
            if data.get('sharenfs', False):
                parts.append('-o sharenfs=on'.format(mount=mount))
            parts.append('{name}{mount}'.format(name=pool_name, mount=mount))
            cmd = ' '.join(parts)
            actions['zfs_mount_{mount}'.format(mount=mount)] = {
                'unless': 'zfs list {name}{mount}'.format(name=pool_name, mount=mount),
                'command': 'rm -rf {mount} && {cmd}'.format(mount=mount, cmd=cmd),
                'needs': ['action:zpool_create_{name}'.format(name=pool_name)],
                'needed_by': ['svc_systemd:'],
            }
