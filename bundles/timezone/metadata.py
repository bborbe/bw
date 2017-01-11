def iptables(metadata):
    if metadata.get('timemachine', {}).get('enabled', False):
        rules = [
            # allow netatalk
            '-A INPUT -m state --state NEW -p tcp --dport 548 -j ACCEPT',
        ]
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', [])
        for i in rules:
            if i not in list:
                list.append(i)
    return metadata
