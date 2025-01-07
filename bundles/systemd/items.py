if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}
files = {}

actions['systemd-reload'] = {
    'command': 'systemctl daemon-reload',
    'triggered': True,
}

files['/etc/systemd/journald.conf'] = {
    'source': 'journald.conf',
    'mode': '0644',
    'owner': 'root',
    'group': 'root',
}
