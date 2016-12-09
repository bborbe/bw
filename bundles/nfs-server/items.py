os = node.metadata.get('os', '')
release = node.metadata.get('release', '')
if os != 'ubuntu' or release != 'xenial':
    raise Exception('{} {} is not supported by this bundle'.format(os, release))

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
    files['/etc/exports'] = {
        'source': 'exports',
        'content_type': 'mako',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'context': {
            'exports': node.metadata.get('nfs-server', {}).get('exports', {}),
        },
        'triggers': ['svc_systemd:nfs-server:restart'],
    }
