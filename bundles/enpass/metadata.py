@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    pkgs = (
        'enpass',
        'libxcb-icccm4',
        'libxcb-image0',
        'libxcb-keysyms1',
        'libxcb-render-util0',
    )
    result = {
        'apt': {
            'packages': {}
        }
    }
    for package_name in pkgs:
        result['apt']['packages'][package_name] = {
            'installed': metadata.get('enpass', {}).get('enabled', False)
        }
    return result


@metadata_reactor.provides(
    'apt/repos/enpass',
)
def enpass_repo(metadata):
    if metadata.get('enpass', {}).get('enabled', False):
        return {
            'apt': {
                'repos': {
                    'enpass': {
                        'installed': True,
                        # 'gpg_key': 'B6DA722E2E65721AF54B93966F7565879798C2FC',
                        'url_key': 'https://apt.enpass.io/keys/enpass-linux.key',
                        'sources': [
                            'deb [arch=amd64 signed-by=/etc/apt/keyrings/enpass.pub] https://apt.enpass.io/ stable main'],
                    },
                }
            }
        }
    else:
        return {}
