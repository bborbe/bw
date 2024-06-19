@metadata_reactor
def docker_repo(metadata):
    if metadata.get('docker', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'docker': {
                        'installed': True,
                        'gpg_key': '9DC858229FC7DD38854AE2D88D81803C0EBFCD88',
                        'sources': ['deb [arch=amd64] https://download.docker.com/linux/ubuntu {} stable'.format(node.metadata.get('release'))],
                    },
                }
            }
        }
    else:
        return {}
