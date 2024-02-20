@metadata_reactor
def install_apt_packages(metadata):
    pkgs = (
        'chromium-browser',
        'gedit',
        'gnome-terminal',
        'ubuntu-desktop',
        'unzip',
        'google-chrome-stable',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result[package_name] = {
            'installed': metadata.get('ubuntu-desktop', {}).get('enabled', False)
        }
    return result


@metadata_reactor
def google_chrome_repo(metadata):
    if metadata.get('ubuntu-desktop', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'google-chrome': {
                        'installed': True,
                        'gpg_key': 'E88979FB9B30ACF2',
                        'sources': ['deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'],
                        #'sources': ['deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main'],
                    },
                }
            }
        }
    else:
        return {}
