@metadata_reactor
def init(metadata):
    return {
        'iptables': {
            'nat_interfaces': set(),
            'mangle': set(),
            'nat': set(),
            'filter': set(),
        },
    }
