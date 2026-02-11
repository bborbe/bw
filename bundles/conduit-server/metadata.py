defaults = {
    'conduit-server': {
        'enabled': False,
        'server_name': 'localhost',
        'port': 8448,
        'version': 'latest',
        'allow_registration': 'true',
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
