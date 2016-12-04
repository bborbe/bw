nodes['nc.v22016124049440903'] = {
    'hostname': 'v22016124049440903.goodsrv.de',
    'metadata': {
        'os': 'ubuntu',
        'release': 'xenial',
        'docker': True,
        'kubernetes': True,
        'openvpn': True,
        'zfs': True,
        'zfs_device': '/dev/sda4',
        'iptables': {
            'enabled': True,
            'rules': [
                'iptables -t nat -A PREROUTING -p tcp -d 185.170.112.48 --dport 80 -j DNAT --to-destination 185.170.112.48:30080',
                'iptables -t nat -A PREROUTING -p tcp -d 185.170.112.48 --dport 443 -j DNAT --to-destination 185.170.112.48:30443',
            ],
        }
    },
}
