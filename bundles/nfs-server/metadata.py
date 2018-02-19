@metadata_processor
def iptables(metadata):
    if metadata.get('nfs-server', {}).get('enabled', False):
        rules = [
            # Portmap ports
            '-A INPUT -m state --state NEW -p udp --dport 111 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 111 -j ACCEPT',
            # NFS daemon ports
            '-A INPUT -m state --state NEW -p udp --dport 2049 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 2049 -j ACCEPT',
            # # NFS mountd ports
            '-A INPUT -m state --state NEW -p udp --dport 33333 -j ACCEPT',
            '-A INPUT -m state --state NEW -p tcp --dport 33333 -j ACCEPT',
        ]
        list = metadata.setdefault('iptables', {}).setdefault('rules', {}).setdefault('filter', set())
        for i in rules:
            if i not in list:
                list.add(i)
    return metadata, DONE
