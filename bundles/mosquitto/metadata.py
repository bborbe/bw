@metadata_processor
def iptables(metadata):
    if metadata.get('mosquitto', {}).get('enabled', False):
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', set())
        list.add('-A INPUT -m state --state NEW -p tcp --dport 1883 -j ACCEPT')
    return metadata, DONE
