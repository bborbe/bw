import bwtv as teamvault


@metadata_reactor
def crons(metadata):
    result = {
        'cron': {
            'jobs': {},
        },
    }
    for name, data in metadata.get('dns-update', {}).get('updates', {}).items():
        expression = '/usr/local/bin/dns-update.sh {server} /etc/dns-update/keys/{name} {zone} {node} {ip} >> /var/log/dns-update.log'.format(
            server=data.get('dns-server', ''),
            name=name,
            zone=data.get('zone', ''),
            node=data.get('node', ''),
            ip=data.get('ip-url', ''),
        )
        result['cron']['jobs']['dns-update-{}'.format(data.get('zone', ''))] = {
            'expression': expression,
            'enabled': metadata.get('dns-update', {}).get('enabled', False),
        }
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
