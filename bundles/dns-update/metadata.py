import bwtv as teamvault


@metadata_reactor
def crons(metadata):
    result = {
        'cron': {
            'jobs': {
                'dns-update': {
                    'enabled': metadata.get('dns-update', {}).get('enabled', False),
                }
            },
        },
    }
    for name, data in metadata.get('dns-update', {}).get('updates', {}).items():
        result['cron']['jobs']['dns-update']['expression'] = '/usr/local/bin/dns-update.sh {server} /etc/dns-update/keys/{name} {zone} {node} {ip} >> /var/log/dns-update.log'.format(
            server=data.get('dns-server', ''),
            name=name,
            zone=data.get('zone', ''),
            node=data.get('node', ''),
            ip=data.get('ip-url', ''),
        )
    return result


@metadata_reactor
def update_passwords(metadata):
    result = {
        'dns-update': {
            'updates': {}
        }
    }
    for name, data in metadata.get('dns-update', {}).get('updates', {}).items():
        result['dns-update']['updates'][name] = {}
        if 'private_hash' in data:
            result['dns-update']['updates'][name]['private'] = teamvault.file(data['private_hash'], site='benjamin-borbe')
        if 'key_hash' in data:
            result['dns-update']['updates'][name]['key'] = teamvault.file(data['key_hash'], site='benjamin-borbe')
    return result
