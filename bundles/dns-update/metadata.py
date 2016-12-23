def crons(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    dns_update = metadata.get('dns-update', {})
    for name, data in dns_update.get('updates', {}).items():
        metadata['cron']['jobs']['dns-update-{name}'.format(name=name)] = {
            'enabled': dns_update.get('enabled', False),
            'expression': '/usr/local/bin/dns-update.sh {server} /etc/dns-update/keys/{name} {zone} {node} {ip}> /dev/null'.format(
                server=data.get('dns-server', ''),
                name=name,
                zone=data.get('zone', ''),
                node=data.get('node', ''),
                ip=data.get('ip-url', ''),
            )
        }
    return metadata
