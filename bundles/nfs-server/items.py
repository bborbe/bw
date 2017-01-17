if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {}
files = {}
directories = {}
actions = {}
pkg_apt = {}

pkg_apt['nfs-kernel-server'] = {
    'installed': node.metadata.get('nfs-server', {}).get('enabled', False),
}

if node.metadata.get('nfs-server', {}).get('enabled', False):
    svc_systemd['nfs-server'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:nfs-kernel-server'],
    }
else:
    svc_systemd['nfs-server'] = {
        'running': False,
        'enabled': False,
    }

if node.metadata.get('nfs-server', {}).get('enabled', False):
    exports = []
    for export, data in node.metadata.get('nfs-server', {}).get('exports', {}).items():
        line = export
        for host, options in sorted(data.items()):
            line += ' {host}({options})'.format(host=host, options=','.join(options))
        exports.append(line)
    files['/etc/exports'] = {
        'source': 'exports',
        'content_type': 'mako',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'context': {
            'exports': exports,
        },
        'triggers': ['svc_systemd:nfs-server:restart'],
    }
    files['/etc/default/nfs-kernel-server'] = {
        'source': 'nfs-kernel-server',
        'content_type': 'mako',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'context': {},
        'triggers': ['svc_systemd:nfs-server:restart'],
    }
