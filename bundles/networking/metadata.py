@metadata_reactor
def defaultnameservers(metadata):
    return {
        'networking': {
            'nameservers': set(['8.8.4.4', '8.8.8.8']),
        }
    }


@metadata_reactor
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
