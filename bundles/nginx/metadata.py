@metadata_processor
def iptables(metadata):
    if metadata.get('nginx', {}).get('enabled', False):
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', set())
        for name, data in metadata.get('nginx', {}).get('vhosts', {}).items():
            list.add('-A INPUT -m state --state NEW -p tcp --dport {} -j ACCEPT'.format(data.get('port', 80)))
    return metadata, DONE
