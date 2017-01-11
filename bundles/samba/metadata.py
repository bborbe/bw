def iptables(metadata):
    if metadata.get('samba', {}).get('enabled', False):
        rules = [
            '-A INPUT -m state --state NEW -p udp --dport 137 -j ACCEPT',
            '-A INPUT -m state --state NEW -p udp --dport 138 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 139 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 445 -j ACCEPT',
        ]
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', [])
        for i in rules:
            if i not in list:
                list.append(i)
    return metadata
