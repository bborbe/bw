@metadata_reactor
def install_apt_packages(metadata):
    pkgs_install = (
        'python3-pip',
        'virtualenv',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs_install:
        result['apt']['packages'][package_name] = {
            'installed': True
        }
    return result
