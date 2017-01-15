if not (node.os == 'ubuntu' and node.os_version == (16, 4) or node.os == 'debian' and node.os_version == (8, 0)):
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}
files = {}
directories = {}

pkg_apt['netatalk'] = {
    'installed': node.metadata.get('timemachine', {}).get('enabled', False),
}

pkg_apt['avahi-daemon'] = {
    'installed': node.metadata.get('timemachine', {}).get('enabled', False),
}

if node.metadata.get('timemachine', {}).get('enabled', False):
    svc_systemd['netatalk'] = {
        'running': True,
        'enabled': True,
        'needs': ['pkg_apt:netatalk', 'file:/etc/netatalk/AppleVolumes.default'],
    }
else:
    svc_systemd['netatalk'] = {
        'running': False,
        'enabled': False,
    }



if node.metadata.get('timemachine', {}).get('enabled', False):
    tu = {}
    needs = ['pkg_apt:netatalk']
    for username, data in node.metadata.get('timemachine', {}).get('users', {}).items():
        needs.append('user:{username}'.format(username=username))
        path = data.get('path', '')
        if len(path) == 0:
            raise Exception('path missing')
        size = data.get('size', '')
        if len(size) == 0:
            raise Exception('size missing')
        tu[username] = {
            'path': path,
            'size': size,
        }
    files['/etc/netatalk/AppleVolumes.default'] = {
        'source': 'AppleVolumes.default',
        'content_type': 'mako',
        'mode': '0644',
        'owner': 'root',
        'group': 'root',
        'context': {
            'users': tu,
        },
        'needs': needs,
        'triggers': ['svc_systemd:netatalk:restart'],
    }
else:
    files['/etc/netatalk/AppleVolumes.default'] = {
        'delete': True,
    }
