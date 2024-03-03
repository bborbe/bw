@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('k3s', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 2379 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 2380 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 8472 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 10250 -j ACCEPT')
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 30000:32767 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
