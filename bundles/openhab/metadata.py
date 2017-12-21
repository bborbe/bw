@metadata_processor
def user(metadata):
    if metadata.get('openhab', {}).get('enabled', False):
        metadata.setdefault('users', {}).setdefault('openhab', {
            'enabled': True,
        })
    return metadata, DONE


@metadata_processor
def iptables(metadata):
    if metadata.get('openhab', {}).get('enabled', False):
        rules = [
            # openHAB ports
            '-A INPUT -m state --state NEW -p tcp --dport 8080 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 8443 -j ACCEPT',
        ]
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', [])
        for i in rules:
            if i not in list:
                list.append(i)
    return metadata, DONE
