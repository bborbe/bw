if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {}
files = {}
pkg_apt = {}
directories = {}

pkg_apt['samba'] = {
    'installed': node.metadata.get('samba', {}).get('enabled', False),
}

if node.metadata.get('samba', {}).get('enabled', False):
    svc_systemd['smbd'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:samba'],
    }
    svc_systemd['nmbd'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:samba'],
    }
else:
    svc_systemd['smbd'] = {
        'running': False,
        'enabled': False,
    }
    svc_systemd['nmbd'] = {
        'running': False,
        'enabled': False,
    }

if node.metadata.get('samba', {}).get('enabled', False):
    files['/etc/samba/smb.conf'] = {
        'source': 'smb.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'server_name': node.metadata.get('samba', {}).get('server_name', ''),
        },
        'needs': ['pkg_apt:samba'],
        'triggers': [
            'svc_systemd:smbd:restart',
            'svc_systemd:nmbd:restart',
        ],
    }
else:
    files['/etc/samba/smb.conf'] = {
        'delete': True,
    }
