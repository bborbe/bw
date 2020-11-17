@metadata_reactor
def install_curl(metadata):
    return {
        'apt': {
            'packages': {
                'curl': {
                    'installed': True
                }
            }
        }
    }
