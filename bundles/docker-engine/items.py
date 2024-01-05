if node.os != 'ubuntu' and node.os != 'raspbian':
    raise Exception('{} {} is not supported by this bundle'.format(node.os, node.os_version))

pkg_apt = {}
svc_systemd = {}

if node.metadata.get('docker', {}).get('enabled', False):
    pkg_apt['docker-ce'] = {
        'installed': True,
    }
    pkg_apt['docker.io'] = {
        'installed': False,
    }
else:
    pkg_apt['docker'] = {
        'installed': False,
    }
