if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}
files = {}
svc_systemd = {}

actions['systemd-reload'] = {
    'command': 'systemctl daemon-reload',
    'triggered': True,
}

svc_systemd['systemd-logind'] = {
    'running': True,
    'enabled': True,
}

files['/etc/systemd/logind.conf'] = {
    'source': 'logind.conf',
    'content_type': 'mako',
    'context': {
        'disablePowerButton': node.metadata.get('systemd', {}).get('disable-power-button', False),
    },
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
    'triggers': [
        'svc_systemd:systemd-logind:restart',
    ],
}

files['/etc/systemd/journald.conf'] = {
    'source': 'journald.conf',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
}
