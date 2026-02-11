defaults = {
    'conduit-server': {
        'enabled': False,
        'server_name': 'localhost',
        'port': 8448,
        'version': 'v0.10.11',
        'allow_registration': 'false',
        'allow_federation': 'false',
        'well_known_base_domain': None,  # e.g. 'benjamin-borbe.de' for @user:benjamin-borbe.de
        'well_known_ip': '0.0.0.0',  # IP to listen on for well-known vhost
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


@metadata_reactor
def nginx_well_known(metadata):
    """Add nginx vhost for Matrix well-known delegation on base domain."""
    conduit = metadata.get('conduit-server', {})
    if not conduit.get('enabled', False):
        return {}
    
    base_domain = conduit.get('well_known_base_domain')
    if not base_domain:
        return {}
    
    server_name = conduit.get('server_name', 'localhost')
    ip = conduit.get('well_known_ip', '0.0.0.0')
    
    # JSON responses for well-known endpoints
    server_json = f'{{"m.server": "{server_name}:443"}}'
    client_json = f'{{"m.homeserver": {{"base_url": "https://{server_name}"}}}}'
    
    return {
        'nginx': {
            'enabled': True,
            'vhosts': {
                f'matrix-well-known-{base_domain}': {
                    'ip': ip,
                    'server_names': [base_domain],
                    'ssl': {
                        'force': True,
                        'cert': f'/etc/letsencrypt/live/{base_domain}/fullchain.pem',
                        'key': f'/etc/letsencrypt/live/{base_domain}/privkey.pem',
                    },
                    'locations': {
                        '/.well-known/matrix/server': {
                            'return': f"200 '{server_json}'",
                            'add_header Content-Type': 'application/json',
                        },
                        '/.well-known/matrix/client': {
                            'return': f"200 '{client_json}'",
                            'add_header Content-Type': 'application/json',
                            'add_header Access-Control-Allow-Origin': '*',
                        },
                        '/': {
                            'return': '404',
                        },
                    },
                    'indexes': [],
                },
            },
        },
    }
