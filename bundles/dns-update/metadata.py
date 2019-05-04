import bwtv as teamvault

@metadata_processor
def crons(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    dns_update = metadata.get('dns-update', {})
    for name, data in dns_update.get('updates', {}).items():
        if 'private_hash' in data:
            data['private'] = teamvault.file(data['private_hash'], site='benjamin-borbe')
        if 'key_hash' in data:
            data['key'] = teamvault.file(data['key_hash'], site='benjamin-borbe')
        metadata['cron']['jobs']['dns-update'] = {
            'enabled': dns_update.get('enabled', False),
            'expression': '/usr/local/bin/dns-update.sh {server} /etc/dns-update/keys/{name} {zone} {node} {ip} >> /var/log/dns-update.log'.format(
                server=data.get('dns-server', ''),
                name=name,
                zone=data.get('zone', ''),
                node=data.get('node', ''),
                ip=data.get('ip-url', ''),
            )
        }
    return metadata, DONE
