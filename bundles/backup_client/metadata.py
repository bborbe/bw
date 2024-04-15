@metadata_reactor.provides(
    'users/root/authorized_keys',
)
def add_backup_key(metadata):
    if metadata.get('backup_client', {}).get('enabled', False) is False:
        return {}
    return {
        'users': {
            'root': {
                'authorized_keys': {
                    'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIqyTzEUpNQn71qYluqEZ4K/ZBchYWqvgm+lZZI3oDgx benjamin.borbe@gmail.com': {},
                }
            }
        }
    }


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if metadata.get('backup_client', {}).get('enabled', False) is False:
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
