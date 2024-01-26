@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('docker-registry', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 5000 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
