def crons(metadata):
    metadata.setdefault('cron', {}).setdefault('jobs', {})
    for name, data in metadata.get('dns-update', {}).items():
        metadata['cron']['jobs']['dns-update-{name}'.format(name=name)] = '* * * * * root /usr/local/bin/dns-update.sh {server} /etc/dns-update/keys/{name} {zone} {node} {ip}> /dev/null'.format(
            server=data.get('dns-server', ''),
            name=name,
            zone=data.get('zone', ''),
            node=data.get('node', ''),
            ip=data.get('ip-url', ''),
        )
    return metadata
