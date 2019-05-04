@metadata_processor
def install_apt_packages(metadata):
    pkgs = (
        'chromium-browser',
        'gedit',
        'gnome-terminal',
        'ubuntu-desktop',
        'unzip',
    )

    for package_name in pkgs:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {})
        metadata['apt']['packages'][package_name]['installed'] = \
            metadata['apt']['packages'][package_name].get('installed', False) or metadata.get('ubuntu-desktop', {}).get('enabled', False)
    return metadata, DONE
