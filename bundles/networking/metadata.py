@metadata_reactor.provides(
    'networking/nameservers',
)
def defaultnameservers(metadata):
    if metadata.get('networking', {}).get('enabled', False):
        return {
            'networking': {
                'nameservers': {'8.8.4.4', '8.8.8.8'},
            }
        }
    return {}


@metadata_reactor.provides(
    'sysctl/options',
)
def enable_routing(metadata):
    if metadata.get('networking', {}).get('enabled', False):
        return {
            'sysctl': {
                'options': {
                    'net.ipv4.ip_forward': '1'
                }
            }
        }
    return {}
