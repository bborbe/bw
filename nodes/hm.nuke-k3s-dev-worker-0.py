# nuke-k3s-dev-worker-0 (.34) — new dev cluster worker (k3s agent, node_type=dev).
# Cloned from hm.nuke-k3s-dev-0.py (agent template). bw owns netplan (durable static
# IP → no cloud-init DHCP race) + k3s (enabled+agent → won't stop it).
# BOOTSTRAP: `username: install` for the first `bw apply`; after it creates bborbe,
# remove `username` + set install.enabled False.
nodes['hm.nuke-k3s-dev-worker-0'] = {
    'hostname': 'nuke-k3s-dev-worker-0.hm.benjamin-borbe.de',
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
                    'addresses': ['192.168.178.34/24'],
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
            'agent': True,
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
            'rules': {'filter': set()},
        },
        'users': {
            'bborbe': {'enabled': True, 'groups': ['sudo']},
            'install': {'enabled': True},  # flip False after first apply
        },
    },
}
