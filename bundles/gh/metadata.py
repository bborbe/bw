@metadata_reactor.provides(
    'apt/repos/gh',
)
def gh_repo(metadata):
    if metadata.get('gh', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'gh': {
                        'installed': True,
                        'url_key': 'https://cli.github.com/packages/githubcli-archive-keyring.gpg',
                        'sources': [
                            'deb [arch=amd64 signed-by=/etc/apt/keyrings/gh.pub] https://cli.github.com/packages stable main',
                        ],
                    },
                }
            }
        }
    return {}


@metadata_reactor.provides(
    'apt/packages',
)
def install_gh_package(metadata):
    return {
        'apt': {
            'packages': {
                'gh': {
                    'installed': metadata.get('gh', {}).get('enabled', False),
                },
            },
        },
    }
