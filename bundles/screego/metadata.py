@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('screego', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 3478 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 5050 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p udp --dport 50000:50100 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
