defaults = {
    'poste': {
        'enabled': False,
        # bborbe/poste.io tag = {analogic vendor version}-{wrapper git branch}.
        # Custom image (POP3 enabled + clamd off) built from github.com/bborbe/poste.io
        # on top of analogic/poste.io — NOT the public image.
        # https://hub.docker.com/r/bborbe/poste.io/tags
        'version': '2.5.13-2.0.1',
        'admin_port': 8001,  # host port -> container :80 (HTTP admin UI; nginx 'mail' vhost proxies this)
    },
}


@metadata_reactor
def iptables(metadata):
    rules = set()
    if metadata.get('poste', {}).get('enabled', False):
        # SMTP 25, SMTPS 465, submission 587, IMAPS 993 — must reach the MTA.
        for port in (25, 465, 587, 993):
            rules.add('-A INPUT -m state --state NEW -p tcp --dport %d -j ACCEPT' % port)
    return {
        'iptables': {
            'rules': {
                'filter': rules,
            },
        },
    }
