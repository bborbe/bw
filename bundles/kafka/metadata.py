@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('kafka', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 9092 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
