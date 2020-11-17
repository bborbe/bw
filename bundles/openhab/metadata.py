@metadata_reactor
def user(metadata):
    return {
        'users': {
            'openhab': {
                'enabled': metadata.get('openhab', {}).get('enabled', False)
            }
        }
    }


@metadata_reactor
def openhab_repo(metadata):
    return {
        'apt': {
            'repos': {
                'openhab': {
                    'gpg_key': 'A224060A',
                    'sources': ['deb https://dl.bintray.com/openhab/apt-repo2 stable main'],
                    'installed': metadata.get('openhab', {}).get('enabled', False),
                }
            }
        }
    }
