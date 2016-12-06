nodes['nc.v22016124049440903'] = {
    'hostname': 'v22016124049440903.goodsrv.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'docker': True,
        'kubernetes': True,
        'openvpn': True,
        'zfs': {
            'enabled': True,
            'device': '/dev/sda4',
            'mounts': {
                '/var/lib/kubelet': {},
                '/var/lib/docker': {},
            },
        },
        'iptables': {
            'enabled': True,
        },
        'haproxy': {
            'ip': '185.170.112.48',
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
            'config_repo': {
                'branch': 'master',
                'repo': 'https://github.com/bborbe/letsencrypt-nc.git',
            },
        },
    },
}
