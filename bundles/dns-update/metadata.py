@metadata_processor
def crons(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    dns_update = metadata.get('dns-update', {})
    for name, data in dns_update.get('updates', {}).items():
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
