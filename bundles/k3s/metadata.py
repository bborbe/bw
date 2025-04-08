@metadata_reactor.provides(
    'iptables/rules/filter',
)
def iptables(metadata):
    rules = set()
    if metadata.get('k3s', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 6443 -s {} -j ACCEPT'.format(metadata['k3s']['network']))
        rules.add('-A INPUT -m state --state NEW -p udp --dport 8472 -s {} -j ACCEPT'.format(metadata['k3s']['network']))
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 10250 -s {} -j ACCEPT'.format(metadata['k3s']['network']))
        if not metadata.get('k3s', {}).get('agent', False):
            rules.add('-A INPUT -m state --state NEW -p tcp --dport 2379 -s {} -j ACCEPT'.format(metadata['k3s']['network']))
            rules.add('-A INPUT -m state --state NEW -p tcp --dport 2380 -s {} -j ACCEPT'.format(metadata['k3s']['network']))
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
