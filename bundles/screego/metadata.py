defaults = {
    'screego': {
        'enabled': False,
        'version': '1.12.4',  # https://hub.docker.com/r/bborbe/screego/tags
        'external_ip': '0.0.0.0',  # SCREEGO_EXTERNAL_IP — node's public IP
        'secret': None,       # SCREEGO_SECRET — from TeamVault (set in node metadata)
        'users_file': None,   # "<name>:<bcrypt>" content — from TeamVault (set in node metadata)
    },
}


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
