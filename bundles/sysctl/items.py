os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

svc_systemd = {
    'systemd-sysctl': {
        'running': True,
        'enabled': True,
    },
}

files = {
    '/etc/sysctl.d/60-custom.conf': {
        'content_type': 'mako',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'triggers': ['svc_systemd:systemd-sysctl:restart'],
    },
}
