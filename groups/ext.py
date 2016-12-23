import bwtv as teamvault

groups['ext'] = {
    'members': [
        'hm.fire',
        'hm.rasp',
        'pn.sun',
        'sm.devel',
        'sm.tools',
    ],
    'bundles': (
        'base',
        'user',
        'sudo',
        'backup',
        'monit',
        'authorized_key',
        'ssh',
        'apt',
        'puppet',
        'hostname',
        'kvm',
        'openvpn',
        'cron',
        'docker-compose',
        'docker-engine',
        'docker-login',
        'locale',
        'kubernetes',
        'ntp',
        'zfs',
        'iptables',
        'haproxy',
        'git',
        'letsencrypt',
        'dhcpclient',
        'sysctl',
        'systemd',
        'nfs-server',
        'dotfiles',
        'networking',
        'dns-update',
    ),
    'metadata': {
        'monit': {
            'enabled': True,
            'sender': teamvault.username('KwRoO7', site='benjamin-borbe'),
            'recipient': 'bborbe@rocketnews.de',
            'server': 'mail.benjamin-borbe.de',
            'port': 587,
            'username': teamvault.username('KwRoO7', site='benjamin-borbe'),
            'password': teamvault.password('KwRoO7', site='benjamin-borbe'),
        },
    },
}
