import bwtv as teamvault

nodes['hz.hetzner-2'] = {
    'hostname': 'hetzner-2.benjamin-borbe.de',
    'groups': {
        'ubuntu-noble',
    },
    'metadata': {
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': True,
                    'dhcp6': False,
                },
            },
        },
        'workspace': {
            'enabled': True,
        },
        'docker': {
            'enabled': True,
        },
        'valheim': {
            'enabled': True,
            'world_name': 'Valheim',
            'server_password': teamvault.password('eOBZ4O', site='benjamin-borbe'),
        },
        'openclaw': {
            'enabled': False,
            'matrix': {
                'enabled': True,
                'homeserver': 'https://matrix.benjamin-borbe.de',
                'user_id': teamvault.username('7qGn5L', site='benjamin-borbe'),
                'password': teamvault.password('7qGn5L', site='benjamin-borbe'),
            },
        },
        'hermes': {
            'enabled': False,
            'matrix': {
                'enabled': True,
                'homeserver': 'https://matrix.benjamin-borbe.de',
                'user_id': teamvault.username('VO053L', site='benjamin-borbe'),
                'password': teamvault.password('VO053L', site='benjamin-borbe'),
            },
            'brave': {
                'enabled': True,
                'api_key': teamvault.password('dwkkzw', site='benjamin-borbe'),
            },
            'telegram': {
                'enabled': True,
                'bot_token': teamvault.password('XO7Qxq', site='benjamin-borbe'),
                'allowed_users': '112230768',  # @bborbe numeric ID — survives handle changes
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    # '-A FORWARD -j ACCEPT',
                    # '-A FORWARD -i tun0 -o tun0 -j DROP',
                },
            },
        },
        'users': {
            'bborbe': {
                'enabled': True,
            },
            # Runs the Valheim server. docker-group membership is root-equivalent on
            # this host — accepted because hetzner-2 is a game/assistant box, not
            # infrastructure. No 'sudo': True: that key grants ALL=(ALL) NOPASSWD: ALL
            # via bundles/sudo/files/users, which would defeat the narrow drop-in.
            'valheim': {
                'enabled': True,
                'uid': 11022,
                'groups': ['docker'],
            },
        },
        'kubectl': {
            'enabled': True,
            'version': 'v1.35',
        },
        'golang': {
            'enabled': True,
            'arch': 'amd64',
            'os': 'linux',
        },
        'trivy': {
            'enabled': True,
        },
        'backup_client': {
            'enabled': True,
        },
    },
}
