@metadata_reactor.provides(
    'iptables/rules/filter',
)
def iptables(metadata):
    if metadata.get('trading', {}).get('enabled', False):
        rules = set()
        # develop ports
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 20000:21000 -j ACCEPT')
        # prod ports
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 30000:31000 -j ACCEPT')
        return {
            'iptables': {
                'rules': {
                    'filter': rules,
                },
            },
        }
    return {}
