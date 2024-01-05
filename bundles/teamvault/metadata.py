@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('teamvault', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 8000 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
