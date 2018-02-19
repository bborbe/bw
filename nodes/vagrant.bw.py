nodes['vagrant.bw'] = {
    'hostname': 'vagrant.bw',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'openhab': {
            'enabled': True,
            'telegram': {
                'hausalertbot': {
                    'chatId': teamvault.username('pLvYPO', site='benjamin-borbe'),
                    'token': teamvault.password('pLvYPO', site='benjamin-borbe'),
                },
            },
            'mosquitto': {
                'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
                'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            },
        },
        'iptables': {
            'enabled': True,
        },
        'nginx': {
            'enabled': True,
            'vhosts': {
                'openhab': {
                    'locations': {
                        '/': [
                            ('proxy_pass', 'http://localhost:8080/'),
                            ('proxy_set_header', 'Host $http_host'),
                            ('proxy_set_header', 'X-Real-IP $remote_addr'),
                            ('proxy_set_header', 'X-Forwarded-For $proxy_add_x_forwarded_for'),
                            ('proxy_set_header', 'X-Forwarded-Proto $scheme'),
                        ],
                    },
                },
            },
        },
        'mosquitto': {
            'enabled': True,
            'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
        },
    },
}
