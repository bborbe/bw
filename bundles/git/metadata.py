@metadata_reactor.provides(
    'apt/packages',
)
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
