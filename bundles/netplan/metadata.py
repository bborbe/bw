@metadata_reactor.provides(
    'sysctl/options',
)
def enable_routing(metadata):
    if metadata.get('netplan', {}).get('enabled', False):
        return {
            'sysctl': {
                'options': {
                    'net.ipv4.ip_forward': '1'
                }
            }
        }
    return {}


@metadata_reactor.provides(
    'apt/packages',
)
def install_apt_packages(metadata):
    result = {
        'apt': {
            'packages': {}
        }
    }
    if metadata.get('netplan', {}).get('enabled', False):
        result['apt']['packages']['resolvconf'] = {
            'installed': False,
        }
        result['apt']['packages']['network-manager'] = {
            'installed': False,
        }
        result['apt']['packages']['bridge-utils'] = {
            'installed': True,
        }
    return result
