import bwtv as teamvault

groups['private'] = {
    'members': [
        'hm.fire',
        'hm.rasp',
        'hm.nuke',
        'pn.sun',
        'sm.devel',
        'sm.tools',
    ],
    'bundles': (
        'backup',
        'cron',
        'dhcpclient',
        'dns-update',
        'docker-compose',
        'docker-engine',
        'docker-login',
        'grub',
        'haproxy',
        'hostname',
        'iptables',
        'kernel_modules',
        'kubernetes',
        'kvm',
        'locale',
        'monit',
        'networking',
        'nfs-server',
        'ntp',
        'openvpn',
        'puppet',
        'smart',
        'ssh',
        'sudo',
        'sysctl',
        'timemachine',
        'timezone',
        'zfs',
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
