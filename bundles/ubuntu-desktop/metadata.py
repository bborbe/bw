@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'gedit',
        'gnome-terminal',
        'ubuntu-desktop',
        'unzip',
        'google-chrome-stable',
        'enpass',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('ubuntu-desktop', {}).get('enabled', False)
        }
    return result


@metadata_reactor.provides(
    'apt/repos/google-chrome',
)
def google_chrome_repo(metadata):
    if metadata.get('ubuntu-desktop', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'google-chrome': {
                        'installed': True,
                        'gpg_key': 'EB4C1BFD4F042F6DDDCCEC917721F63BD38B4796',
                        'sources': ['deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'],
                    },
                }
            }
        }
    else:
        return {}



@metadata_reactor.provides(
    'apt/repos/enpass',
)
def enpass_repo(metadata):
    if metadata.get('ubuntu-desktop', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'enpass': {
                        'installed': True,
                        'gpg_key': 'B6DA722E2E65721AF54B93966F7565879798C2FC',
                        'sources': ['deb https://apt.enpass.io/  stable main'],
                    },
                }
            }
        }
    else:
        return {}


