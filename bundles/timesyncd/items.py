if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {
    'systemd-timesyncd': {
        'running': True,
        'enabled': True,
    },
}

pkg_apt = {
    'ntpdate': {
        'installed': False,
    },
}

actions = {
    'remove-ntpdate-cron': {
        'command': 'rm -f /etc/cron.d/ntpdate',
        'unless': 'test ! -f /etc/cron.d/ntpdate',
    },
}
