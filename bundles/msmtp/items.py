if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
files = {}

pkg_apt['msmtp'] = {
    'installed': node.metadata.get('msmtp', {}).get('enabled', False),
}

pkg_apt['msmtp-mta'] = {
    'installed': node.metadata.get('msmtp', {}).get('enabled', False),
}

if node.metadata.get('msmtp', {}).get('enabled', False):
    files['/etc/msmtprc'] = {
        'source': 'msmtprc',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'host': node.metadata.get('msmtp', {}).get('host', '172.16.90.1'),
            'port': node.metadata.get('msmtp', {}).get('port', 25),
            'from_addr': node.metadata.get('msmtp', {}).get('from', 'root@{}'.format(node.hostname)),
        },
    }
else:
    files['/etc/msmtprc'] = {
        'delete': True,
    }
