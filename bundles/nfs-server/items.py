os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

files = {}

pkg_apt = {
    'nfs-kernel-server': {
        'installed': node.metadata.get('nfs-server', {}).get('enabled', False),
    },
}

svc_systemd = {
    'nfs-kernel-server': {
        'running': node.metadata.get('nfs-server', {}).get('enabled', False),
        'enabled': node.metadata.get('nfs-server', {}).get('enabled', False),
        'needs': ['pkg_apt:nfs-kernel-server'],
    },
}

if node.metadata.get('nfs-server', {}).get('enabled', False):
    files['/etc/exports'] = {
        'source': 'exports',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {},
        'needs': ['pkg_apt:nfs-kernel-server'],
        'triggers': ['svc_systemd:nfs-kernel-server:restart'],
    }
else:
    files['/etc/exports'] = {
        'delete': True,
    }
