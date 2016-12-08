nodes['nc.v22016124049440903'] = {
    'hostname': 'v22016124049440903.goodsrv.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'docker': {
            'enabled': True,
        },
        'kubernetes': True,
        'openvpn': True,
        'zfs': {
            'enabled': True,
            'device': '/dev/sda4',
            'mounts': {
                '/data': {
                    'sharenfs': True,
                },
                '/var/lib/kubelet': {},
                '/var/lib/docker': {},
            },
        },
        'haproxy': {
            'ip': '185.170.112.48',
            'enabled': True,
        },
        'letsencrypt': {
            'enabled': True,
            'email': 'bborbe@rocketnews.de',
            'domains': {
                'benjamin-borbe.de': ['www.benjamin-borbe.de', 'password.benjamin-borbe.de', 'ip.benjamin-borbe.de', 'test.benjamin-borbe.de', 'backup.benjamin-borbe.de', 'blog.benjamin-borbe.de', 'confluence.benjamin-borbe.de',
                                      'kickstart.benjamin-borbe.de', 'ks.benjamin-borbe.de', 'nsqadmin.benjamin-borbe.de', 'prometheus.benjamin-borbe.de', 'slideshow.benjamin-borbe.de', 'taiga.benjamin-borbe.de', 'wiki.benjamin-borbe.de',
                                      'webdav.benjamin-borbe.de', 'booking.benjamin-borbe.de', 'grafana.benjamin-borbe.de', 'dashboard.benjamin-borbe.de', 'mail.benjamin-borbe.de', 'auth.benjamin-borbe.de', 'kibana.benjamin-borbe.de',
                                      'elasticsearch.benjamin-borbe.de', 'prometheus-alertmanager.benjamin-borbe.de', 'teamvault.benjamin-borbe.de', 'jana-und-ben.benjamin-borbe.de'],
                'benjaminborbe.de': ['www.benjaminborbe.de'],
                'harteslicht.de': ['www.harteslicht.de', 'blog.harteslicht.de'],
                'harteslicht.com': ['www.harteslicht.com', 'blog.harteslicht.com'],
                'rocketnews.de': ['www.rocketnews.de'],
                'rocketsource.de': ['www.rocketsource.de'],
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': ['ens3'],
            'rules': [
                # allow forward
                'iptables -A CUSTOM-FORWARD -j ACCEPT',

                # Http + Https
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 443 -j ACCEPT',

                # K8s
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 6443 -j ACCEPT',

                # Smtp + Smtps
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 25 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 465 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 587 -j ACCEPT',

                # Imap + Imaps
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 143 -j ACCEPT',
                'iptables -A CUSTOM-INPUT -m state --state NEW -p tcp --dport 993 -j ACCEPT',
            ],
        },
        'sysctl': {
            'options': {
                # increaese for elasticsearch
                'vm.max_map_count': '262144',
            },
        },
    },
}
