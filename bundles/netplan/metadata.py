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
