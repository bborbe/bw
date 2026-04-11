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
else:
    svc_systemd['smbd'] = {
        'running': False,
        'enabled': False,
    }
    svc_systemd['nmbd'] = {
        'running': False,
        'enabled': False,
    }


def _render_share(name, share):
    lines = [
        '[{}]'.format(name),
        '\tcomment = {}'.format(share.get('comment', name)),
        '\tpath = {}'.format(share['path']),
        '\tbrowsable = {}'.format(share.get('browsable', 'yes')),
        '\tvalid users = {}'.format(share['valid_users']),
        '\tread only = {}'.format(share.get('read_only', 'no')),
        '\tcreate mask = {}'.format(share.get('create_mask', '0660')),
        '\tdirectory mask = {}'.format(share.get('directory_mask', '0770')),
    ]
    if 'force_user' in share:
        lines.append('\tforce user = {}'.format(share['force_user']))
    if 'force_group' in share:
        lines.append('\tforce group = {}'.format(share['force_group']))
    lines.append('\tveto files = /.DS_Store/._*/')
    lines.append('\tdelete veto files = yes')
    return '\n'.join(lines)


def _render_homes(homes):
    users = ' '.join(homes.get('valid_users', []))
    return '\n'.join([
        '[homes]',
        '\tcomment = Home Directories',
        '\tbrowseable = no',
        '\tvalid users = {}'.format(users),
        '\twritable = yes',
        '\tread only = no',
        '\tcreate mask = 0600',
        '\tdirectory mask = 0700',
        '\tveto files = /.DS_Store/._*/',
        '\tdelete veto files = yes',
    ])


if samba_enabled:
    shares = samba_metadata.get('shares', {})
    homes = samba_metadata.get('homes', {})

    blocks = []
    for share_name in sorted(shares.keys()):
        blocks.append(_render_share(share_name, shares[share_name]))
    if homes.get('enabled', False):
        blocks.append(_render_homes(homes))

    files['/etc/samba/smb.conf'] = {
        'source': 'smb.conf',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'server_name': samba_metadata.get('server_name', ''),
            'sections': '\n\n'.join(blocks),
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
