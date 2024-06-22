@metadata_reactor.provides(
    'apt/repos/gcloud-sdk',
)
def google_chrome_repo(metadata):
    if metadata.get('gcloud-sdk', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'gcloud-sdk': {
                        'installed': True,
                        'url_key': 'https://packages.cloud.google.com/apt/doc/apt-key.gpg',
                        'sources': [
                            'deb [signed-by=/etc/apt/keyrings/gcloud-sdk.pub] https://packages.cloud.google.com/apt cloud-sdk main',
                        ],
                    },
                }
            }
        }
    else:
        return {}


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'google-cloud-cli',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('gcloud-sdk', {}).get('enabled', False)
        }
    return result
