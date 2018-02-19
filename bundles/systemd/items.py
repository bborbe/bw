if node.os != 'ubuntu' and node.os != 'debian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

actions = {}

actions['systemd-reload'] = {
    'command': 'systemctl daemon-reload',
    'triggered': True,
}
