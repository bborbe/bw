if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

svc_systemd = {}
files = {}
pkg_apt = {}
directories = {}

samba_metadata = node.metadata.get('samba', {})
samba_enabled = samba_metadata.get('enabled', False)

pkg_apt['samba'] = {
    'installed': samba_enabled,
}

if samba_enabled:
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
    files['/etc/samba/smb.conf'] = {
        'source': 'smb.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'server_name': samba_metadata.get('server_name', ''),
            'shares': samba_metadata.get('shares', {}),
            'homes': samba_metadata.get('homes', {}),
        },
        'needs': ['pkg_apt:samba'],
        'triggers': [
            'svc_systemd:smbd:restart',
            'svc_systemd:nmbd:restart',
        ],
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
    files['/etc/samba/smb.conf'] = {
        'delete': True,
    }
