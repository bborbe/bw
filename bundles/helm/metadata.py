@metadata_reactor.provides(
    'apt/repos/helm',
)
def helm_repo(metadata):
    if metadata.get('helm', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'helm': {
                        'installed': True,
                        'url_key': 'https://baltocdn.com/helm/signing.asc',
                        'gpg_dearmor': True,
                        'sources': [
                            'deb [arch=amd64 signed-by=/etc/apt/keyrings/helm.pub] https://baltocdn.com/helm/stable/debian/ all main',
                        ],
                    },
                }
            }
        }
    return {}


@metadata_reactor.provides(
    'apt/packages',
)
def install_helm_package(metadata):
    return {
        'apt': {
            'packages': {
                'helm': {
                    'installed': metadata.get('helm', {}).get('enabled', False),
                },
            },
        },
    }
