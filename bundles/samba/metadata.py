@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('samba', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p udp --dport 137 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p udp --dport 138 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 139 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 445 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
