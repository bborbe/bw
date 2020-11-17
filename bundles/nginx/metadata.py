@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('nginx', {}).get('enabled', False):
        for name, data in metadata.get('nginx', {}).get('vhosts', {}).items():
            rules.add('-A INPUT -m state --state NEW -p tcp --dport {} -j ACCEPT'.format(data.get('port', 80)))
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
