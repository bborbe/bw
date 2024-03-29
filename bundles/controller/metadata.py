@metadata_reactor
def git_clone_hue(metadata):
    if metadata.get('controller', {}).get('enabled', False):
        return {
            'git': {
                'clones': {
                    'hue': {
                        'repo': 'https://github.com/bborbe/hue.git',
                        'target': '/opt/hue',
                    },
                }
            }
        }
    else:
        return {}


@metadata_reactor
def user_group(metadata):
    return {
        'users': {
            'controller': {
                'enabled': metadata.get('controller', {}).get('enabled', False),
            }
        }
    }
