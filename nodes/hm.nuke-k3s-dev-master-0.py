# nuke-k3s-dev-master-0 (.30) — new dev cluster master (k3s server, SQLite, tainted).
# Cloned from hm.nuke-k3s-prod.py (server template). bw owns netplan (durable static
# IP) + k3s (enabled, server — no agent). node_type=master label + NoSchedule taint
# live on the node object (from install); a k3s restart preserves them.
# BOOTSTRAP: `username: install` for the first `bw apply`; remove + install.enabled
# False after bborbe exists.
nodes['hm.nuke-k3s-dev-master-0'] = {
    'hostname': 'nuke-k3s-dev-master-0.hm.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'optional': True,
                    'match': {'name': 'en*'},
                    'set-name': 'eth0',
                    'addresses': ['192.168.178.30/24'],
                    'routes': [{'to': 'default', 'via': '192.168.178.1'}],
                    'nameservers': {
                        'addresses': ['8.8.8.8', '8.8.4.4'],
                        'search': ['hm.benjamin-borbe.de'],
                    },
                },
            },
        },
        'kvm-guest': {'enabled': True},
        'backup_client': {'enabled': True},
        'k3s': {
            'enabled': True,
            'network': '192.168.178.0/24',
            'config': {
                'kubelet-arg': [
                    'image-gc-high-threshold=80',
                    'image-gc-low-threshold=70',
                    'eviction-hard=imagefs.available<10%',
                    'max-pods=512',
                ]
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': set({
                    '-A INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',
                }),
            },
        },
        'users': {
            'bborbe': {'enabled': True, 'groups': ['sudo']},
            'install': {'enabled': True},  # flip False after first apply
        },
    },
}
