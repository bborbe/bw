defaults = {
    'conduit-server': {
        'enabled': False,
        'server_name': 'localhost',
        'port': 8448,
        'version': 'v0.10.11',
        'allow_registration': 'false',
        'allow_federation': 'false',
    },
}


@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('conduit-server', {}).get('enabled', False):
        port = metadata.get('conduit-server', {}).get('port', 8448)
        rules.add(f'-A INPUT -m state --state NEW -p tcp --dport {port} -j ACCEPT')
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
