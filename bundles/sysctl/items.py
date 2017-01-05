if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {}

files = {}

svc_systemd['systemd-sysctl'] = {
    'running': True,
    'enabled': True,
}

files['/etc/sysctl.d/60-custom.conf'] = {
    'content_type': 'mako',
    'owner': 'root',
    'group': 'root',
    'mode': '0644',
    'triggers': ['svc_systemd:systemd-sysctl:restart'],
}
