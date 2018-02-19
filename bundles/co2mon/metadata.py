@metadata_processor
def install_apt_packages(metadata):
    pkgs = (
        'python3-pip',
        'virtualenv',
    )
    for package_name in pkgs:
        metadata.setdefault('apt', {}).setdefault('packages', {}).setdefault(package_name, {})
        metadata['apt']['packages'][package_name]['installed'] = \
            metadata['apt']['packages'][package_name].get('installed', False) or metadata.get('co2mon', {}).get('enabled', False)
    return metadata, DONE
