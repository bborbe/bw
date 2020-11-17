@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('mosquitto', {}).get('enabled', False):
        rules.add('-A INPUT -m state --state NEW -p tcp --dport 1883 -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
