@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    if len(metadata.get('mdadm', {})) == 0:
        return {}

    return {
        'apt': {
            'packages': {
                'mdadm': {
                    'installed': True
                },
            }
        }
    }
