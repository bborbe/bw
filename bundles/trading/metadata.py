@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('trading', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 20000:21000 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 30000:31000 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
