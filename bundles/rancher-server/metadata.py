@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('samba', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p udp --dport 80 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p udp --dport 443 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
