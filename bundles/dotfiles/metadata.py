@metadata_reactor
def install_git(metadata):
    return {
        'apt': {
            'packages': {
                'git': {
                    'installed': True,
                },
            }
        },
    }

