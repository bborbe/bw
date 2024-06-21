@metadata_reactor.provides(
    'apt/repos/docker',
)
def docker_repo(metadata):
    if metadata.get('docker', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'docker': {
                        'installed': True,
                        'url_key': 'https://download.docker.com/linux/ubuntu/gpg',
                        'sources': [
                            'deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.pub] https://download.docker.com/linux/ubuntu {} stable'.format(node.metadata.get('release'))
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
        'docker-ce',
        'docker-ce-cli',
        'containerd.io',
        'docker-buildx-plugin',
        'docker-compose-plugin',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('docker', {}).get('enabled', False)
        }
    return result
