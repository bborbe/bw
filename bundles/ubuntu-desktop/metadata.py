@metadata_reactor
def install_apt_packages(metadata):
    pkgs = (
        'chromium-browser',
        'gedit',
        'gnome-terminal',
        'ubuntu-desktop',
        'unzip',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result[package_name] = {
            'installed': metadata.get('ubuntu-desktop', {}).get('enabled', False)
        }
    return result
