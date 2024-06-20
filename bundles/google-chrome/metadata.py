@metadata_reactor.provides(
    'apt/repos/google-chrome',
)
def google_chrome_repo(metadata):
    if metadata.get('google-chrome', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'google-chrome': {
                        'installed': True,
                        'url_key': 'https://dl-ssl.google.com/linux/linux_signing_key.pub',
                        'sources': [
                            'deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.pub] http://dl.google.com/linux/chrome/deb/ stable main'],
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
        'google-chrome-stable',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('google-chrome', {}).get('enabled', False)
        }
    return result
