@metadata_processor
def install_apt_packages(metadata):

    pkgs = (
        'chromium-browser',
        'firefox',
        'emacs',
        'gedit',
        'gnome-terminal',
        'indicator-session',
        'lightdm',
        'software-center',
        'ubuntu-desktop',
        'unity-lens-applications',
        'unzip',
    )

    for package_name in pkgs:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {})
        metadata['apt']['packages'][package_name]['installed'] = \
            metadata['apt']['packages'][package_name].get('installed', False) or metadata.get('ubuntu-desktop', {}).get('enabled', False)
    return metadata, DONE
