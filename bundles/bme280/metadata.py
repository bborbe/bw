@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if not metadata.get('bme280', {}).get('enabled', False):
        return {}
    pkgs_install = (
        'python3-pip',
        'virtualenv',
        'i2c-tools',
        'python3-smbus',
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
